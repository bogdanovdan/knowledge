# /// script
# requires-python = ">=3.11"
# dependencies = ["faster-whisper>=1.1"]
# ///
"""Independent check of Gemini transcript timing and wording against local Whisper (free, CPU).

  uv run --script _pipeline/validate_timestamps.py whisper <lesson_id> [--model small.en]
  uv run --script _pipeline/validate_timestamps.py compare <lesson_id>

`whisper` writes _pipeline/validation/<lesson_id>.whisper.json (word-level timestamps).
`compare` aligns the Gemini transcript's words to Whisper's and reports timing offsets and word agreement.
"""
import difflib
import json
import os
import re
import statistics
import sys
import time
from pathlib import Path

HERE = Path(__file__).resolve().parent
LIB = HERE.parent
CACHE = Path(os.environ.get("LOCALAPPDATA", str(Path.home()))) / "OriginsSourceLibrary" / "cache"
VAL = HERE / "validation"


def norm_words(text):
    return re.findall(r"[a-z]+|\d+", text.lower())


def load_audio(path):
    """Decode with ffmpeg to 16 kHz mono float32 (PyAV's DLL is blocked by Windows Application Control here)."""
    import shutil
    import subprocess
    import glob
    import numpy as np

    ff = shutil.which("ffmpeg") or sorted(glob.glob(os.path.expandvars(
        r"%LOCALAPPDATA%\Microsoft\WinGet\Packages\Gyan.FFmpeg*\*\bin\ffmpeg.exe")))[0]
    raw = subprocess.run([ff, "-v", "error", "-i", str(path), "-f", "f32le", "-ac", "1", "-ar", "16000", "-"],
                         capture_output=True, check=True).stdout
    return np.frombuffer(raw, dtype=np.float32)


def run_whisper(lid, model_name):
    import types
    sys.modules.setdefault("av", types.ModuleType("av"))  # faster_whisper imports av at module load
    from faster_whisper import WhisperModel

    audio = load_audio(CACHE / lid / "audio.flac")
    t0 = time.time()
    model = WhisperModel(model_name, device="cpu", compute_type="int8", cpu_threads=os.cpu_count() or 4)
    segs, info = model.transcribe(audio, language="en", word_timestamps=True, vad_filter=False, beam_size=1)
    words, out_segs = [], []
    for s in segs:
        out_segs.append({"start": s.start, "end": s.end, "text": s.text.strip()})
        for w in s.words or []:
            words.append({"start": round(w.start, 2), "end": round(w.end, 2), "word": w.word.strip()})
    VAL.mkdir(parents=True, exist_ok=True)
    out = {"lesson": lid, "model": model_name, "elapsed_s": round(time.time() - t0, 1),
           "duration": info.duration, "segments": out_segs, "words": words}
    (VAL / f"{lid}.whisper.json").write_text(json.dumps(out, indent=1), encoding="utf-8")
    print(f"whisper {model_name}: {len(words)} words in {out['elapsed_s']}s for {info.duration:.0f}s audio")


def compare(lid):
    w = json.loads((VAL / f"{lid}.whisper.json").read_text(encoding="utf-8"))
    g = json.loads((LIB / "lessons" / lid / "transcript.json").read_text(encoding="utf-8"))
    ww = []  # (normalized word, start)
    for x in w["words"]:
        for n in norm_words(x["word"]):
            ww.append((n, x["start"]))
    gw, seg_first = [], {}  # (normalized word, segment index)
    for i, s in enumerate(g["segments"]):
        ns = norm_words(s["text"])
        if ns:
            seg_first[len(gw)] = i
        for n in ns:
            gw.append((n, i))
    sm = difflib.SequenceMatcher(a=[x[0] for x in gw], b=[x[0] for x in ww], autojunk=False)
    gmap = {}
    matched = 0
    for a, b, n in sm.get_matching_blocks():
        for k in range(n):
            gmap[a + k] = b + k
        matched += n
    offsets = []
    worst = []
    for gi, si in seg_first.items():
        if gi in gmap:
            d = g["segments"][si]["start"] - ww[gmap[gi]][1]
            offsets.append(d)
            worst.append((abs(d), g["segments"][si]["start"], ww[gmap[gi]][1], g["segments"][si]["text"][:70]))
    absd = sorted(abs(d) for d in offsets)
    pct = lambda p: absd[min(len(absd) - 1, int(p * len(absd)))] if absd else float("nan")
    rep = {
        "lesson": lid,
        "gemini_words": len(gw), "whisper_words": len(ww),
        "word_agreement_vs_whisper": round(2 * matched / (len(gw) + len(ww)), 3),
        "segments_checked": len(offsets), "segments_total": len(g["segments"]),
        "start_offset_s": {"median_abs": round(pct(0.5), 2), "p90_abs": round(pct(0.9), 2),
                           "max_abs": round(absd[-1], 2) if absd else None,
                           "mean_signed": round(statistics.mean(offsets), 2) if offsets else None,
                           "within_1s": round(sum(1 for d in absd if d <= 1) / max(1, len(absd)), 3),
                           "within_2s": round(sum(1 for d in absd if d <= 2) / max(1, len(absd)), 3)},
        "worst_segments": [{"abs_offset": round(a, 2), "gemini_start": gs, "whisper_start": ws, "text": t}
                           for a, gs, ws, t in sorted(worst, reverse=True)[:8]],
    }
    # passages present in one transcript but not the other (possible omissions / hallucinations)
    gaps = []
    for tag, a0, a1, b0, b1 in sm.get_opcodes():
        if tag in ("delete", "insert", "replace") and max(a1 - a0, b1 - b0) >= 12:
            gaps.append({"type": tag, "gemini_words": a1 - a0, "whisper_words": b1 - b0,
                         "at_whisper_s": ww[min(b0, len(ww) - 1)][1],
                         "gemini_text": " ".join(x[0] for x in gw[a0:a1])[:200],
                         "whisper_text": " ".join(x[0] for x in ww[b0:b1])[:200]})
    rep["long_disagreements"] = gaps
    (VAL / f"{lid}.compare.json").write_text(json.dumps(rep, indent=1), encoding="utf-8")
    print(json.dumps(rep, indent=1))


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    cmd, lid = sys.argv[1], sys.argv[2]
    if cmd == "whisper":
        model = sys.argv[sys.argv.index("--model") + 1] if "--model" in sys.argv else "small.en"
        run_whisper(lid, model)
    else:
        compare(lid)
