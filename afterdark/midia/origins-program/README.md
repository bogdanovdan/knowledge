> **Nota:** os frames (PNG) desta biblioteca ficam no Google Drive, em `Knowledge/afterdark/midia/origins-program/frames` ([abrir pasta](https://drive.google.com/drive/folders/1Uj8jgHgvuemO3v3wTC8ec1J0O65QLy2D)), com um arquivo zip por aula (`<aula>-frames.zip`). Os links nos `visual_notes.md` apontam para o zip da aula. Esta biblioteca registra só o que o curso ensina, não decisões para as marcas da Afterdark.

# Origins Program ($0-$100k/mo) - Source Library

A searchable, timestamped library built from the Evolve course folder
`../Origins Program ($0-$100k mo)/`. The original course files are untouched; everything here is derived.

**Browse by business area:** [Nine categories covering all 90 lessons](categories/README.md).

**Start here:** [INDEX.md](INDEX.md) (every lesson, grouped by course section) · [search.html](search.html)
(open in a browser; searches all transcripts, on-screen notes and lesson pages) ·
[PROCESSING_REPORT.md](PROCESSING_REPORT.md) (completeness, flagged sections, spend).

## Results (built 2026-10-06)

| | |
|---|---|
| Lessons | 90 (68 with video, 28.3 h; 22 text/action-item pages) and 29 templates |
| Transcripts | 360 / 360 audio chunks transcribed (359 on the first attempt, 1 retry, no failures); 17,299 timestamped segments |
| Timing | every lesson aligned to local Whisper word timestamps; median 95% of words matched (lowest 78%, FB setup screen recordings) |
| Completeness checks | 41 words filled in from Whisper (5 places); 269 words of Gemini-invented text removed (3 places, each confirmed by two local models, kept in JSON); 4 passages unconfirmed (crosstalk/Mandarin in the live webinar, kept and flagged); 7 low-confidence possible omissions listed |
| Visual notes | 1,954 screenshots kept from 5,517 visually distinct candidates, each with on-screen text and "not in transcript" notes |
| Summaries | 68, one per video lesson |
| API spend | $16.85 on gemini-3.8-flash: transcription $6.75, visual notes $8.77, summaries $1.33 |

Details per lesson and every flagged time range are in [PROCESSING_REPORT.md](PROCESSING_REPORT.md).
Gemini's recitation filter blocked some frames showing published text (book pages, long reviews); those were
re-described in paraphrase rather than copied verbatim, so no frame was left unreviewed.

## What is in each lesson folder

`lessons/<NNN>-<slug>/`

| File | What it is |
|---|---|
| `transcript.md` | Readable transcript, paragraphs prefixed with `[HH:MM:SS]`. Flagged sections listed at the top. |
| `transcript.json` | Full segment-level transcript (start/end seconds, speaker, text), chunk log, and every quality issue. |
| `transcript.srt` | Subtitles for the original video (load next to the `.mp4` in VLC etc.). |
| `visual_notes.md` / `.json` | Timestamped notes on slides, diagrams, spreadsheets, ad examples and software demos: what is on screen, and what is visible but **not said aloud**. |
| `frames/` | Screenshots referenced by the visual notes, PNG at the video's native resolution (mostly 854×480; some 1280×720). Named `<lesson>_<HH-MM-SS>.png`. |
| `summary.md` | AI summary of the lesson's teachings. Kept separate from the transcript; always check claims against the transcript timestamps. |
| `lesson_page.md` | Text and resource links from the saved Skool lesson page, plus links to the original video, page and templates. |

Lessons without a video (action items, tool/supplier pages) only have `lesson_page.md`.
`templates/` holds plain-text extracts of every `.docx/.xlsx/.pptx/.pdf` in the course folder for searching;
the index links both the extract and the original file.

## Conventions

- **All timestamps refer to the original video timeline** (`HH:MM:SS`, or seconds in JSON).
- Transcripts are verbatim; only pure filler sounds ("um", "uh") may be dropped. `[inaudible]` marks
  unintelligible audio and `word [?]` marks an uncertain word.
- Speaker labels: `Presenter` (main instructor), `Speaker 2`... (others), `Played audio` (ads/videos played in
  the lesson). Labels are assigned per ~5-minute chunk, so in multi-speaker recordings (the live webinar, Q&A)
  the same person can appear under different labels in different chunks (e.g. `Presenter` vs. `Spencer`).
- AI-generated content (transcripts, visual notes, summaries) can contain errors. Figures that matter should be
  checked against the screenshot or the video.

## Scope: course teachings only

This library records **what the course teaches**. It deliberately contains no decisions, plans or adaptations for
Lume or any other business. Those belong in the Lume project (`Projetos/Lume/docs/DECISIONS.md` and related
docs), where course ideas should be treated as external input, not facts.

## How it was built

Pipeline code lives in [`_pipeline/`](_pipeline/) (`origins_pipeline.py`, run with `uv`). Stages:

1. **inventory**: parse the 90 saved Skool pages (titles, sections, text, links), match videos and templates.
2. **prepare** (local, free): extract 16 kHz mono audio with ffmpeg, detect pauses, cut ~5-minute chunks
   **at pauses** so no words are split, and encode each chunk as a small MP3. Whole-video audio is never uploaded.
3. **transcribe** (Gemini API): each chunk is sent separately with a strict verbatim prompt and JSON schema.
   Every API response is saved to `_pipeline/raw/` *before* parsing. Chunk timestamps are shifted back onto the
   original timeline. Each chunk is checked for coverage of speech audio, words-per-minute, repetition loops and
   out-of-range timestamps; failing chunks are retried (up to 3 attempts, then a fallback model) and anything still
   doubtful is flagged rather than hidden.
4. **timing + completeness check** (local, free): a second, independent transcription with
   faster-whisper `base.en` on the CPU (`_pipeline/whisper_timing.py`). Validation on lesson 20 showed that
   Gemini's wording is excellent (~95% word agreement with Whisper, no omitted passages) but its own timestamps
   drift by up to ~28 s inside a 5-minute chunk. So the **text comes from Gemini and the timing from Whisper**:
   Gemini's words are aligned to Whisper's word timestamps, which brought segment start times to within 1 s of
   a `small.en` reference for 99-100% of segments (median error 0.1 s). The same comparison checks completeness
   both ways:
   - speech Whisper heard that is missing from the Gemini text is inserted as *[+ ...]* and flagged;
   - Gemini text Whisper did not hear is re-checked with the stronger `small.en` model (beam search) on that
     window. If `small.en` hears it, it stays unflagged. If neither model hears it, it stays in the transcript
     but is flagged as *unconfirmed* (typically crosstalk, music, played ads or foreign speech).
   - Text is **removed** only when both local models fail to hear it *and* there is no time in the audio in which
     it could have been spoken (it sits squeezed between two well-aligned neighbours). This caught a real case in
     lesson 1, where Gemini had inserted ~96 plausible words that are not in the recording. Removed text is kept in
     `transcript.json` under `removed_segments` and listed in the flagged sections, so nothing disappears silently.
5. **assemble**: merge chunks into JSON, SRT and Markdown, and list gaps or uncertain sections.
6. **frames** (local, free): sample every keyframe (~every 5 s), group frames into visual scenes, and keep the most
   complete frame of each scene as a candidate.
7. **visual** (Gemini API): candidates are reviewed in batches *together with the saved, aligned transcript around
   them* (audio is never re-transcribed). Informative frames are kept, saved as PNG, and annotated. URLs read off
   the screen are checked against the links on the course pages, and the exact link is added when they nearly match.
8. **summarize** (Gemini API), **templates** (local text extraction), **index**. `follow` chains assemble, visual
   and summarize for each lesson as soon as its transcript and Whisper timing are ready.

### Resuming or re-running

```
cd "<this folder>"
uv run --script _pipeline/origins_pipeline.py status        # progress per lesson
uv run --script _pipeline/origins_pipeline.py estimate      # cost estimate for remaining paid work
uv run --script _pipeline/origins_pipeline.py free          # inventory, prepare, frames, templates, index
uv run --script _pipeline/origins_pipeline.py transcribe    # Gemini; skips finished chunks
uv run --python 3.14 --script _pipeline/whisper_timing.py   # local timing pass; skips finished lessons
uv run --script _pipeline/origins_pipeline.py follow        # assemble + visual + summarize as lessons become ready
uv run --script _pipeline/origins_pipeline.py transcribe --retry-failed
uv run --script _pipeline/origins_pipeline.py visual --lessons 20 --redo
```

`whisper_timing.py` runs on the system Python 3.14 because Windows Application Control on this machine blocks
some DLLs in uv's bundled Python 3.12 and in PyAV; audio is decoded with ffmpeg instead.

Progress is tracked per lesson and per chunk in `_pipeline/state/`. API usage and cost are appended to
`_pipeline/state/usage.jsonl`, and a hard cap (`max_cost_usd`) stops paid stages. The working audio and keyframe
cache (~5.3 GB) lives outside OneDrive in `%LOCALAPPDATA%\OriginsSourceLibrary\cache` and can be deleted at any time;
it is rebuilt deterministically from the saved chunk plan. Requirements: `uv`, `ffmpeg` (winget `Gyan.FFmpeg`),
and `GEMINI_API_KEY` in the user environment.
