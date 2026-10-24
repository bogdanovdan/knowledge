# /// script
# requires-python = ">=3.11"
# dependencies = ["faster-whisper>=1.1"]
# ///
"""Local Whisper pass used only for TIMING (free, CPU). Gemini supplies the transcript text; the pipeline's
assemble stage aligns Gemini's words to these word timestamps, and long passages that Whisper hears but Gemini
lacks are flagged as possible omissions.

  uv run --python 3.14 --script _pipeline/whisper_timing.py [--model base.en] [--lessons 20,25]
  uv run --python 3.14 --script _pipeline/whisper_timing.py --verify [--lessons 1]

Writes _pipeline/state/lessons/<id>/whisper_words.json; lessons already done are skipped (resumable).
--verify re-checks suspected inserted text with small.en (see verify()).
Audio comes from the pipeline cache (run the `prepare` stage first).
"""
import glob
import json
import os
import shutil
import subprocess
import sys
import time
import types
from pathlib import Path

HERE = Path(__file__).resolve().parent
STATE = HERE / "state"
CACHE = Path(os.environ.get("LOCALAPPDATA", str(Path.home()))) / "OriginsSourceLibrary" / "cache"


def ffmpeg() -> str:
    return shutil.which("ffmpeg") or sorted(glob.glob(os.path.expandvars(
        r"%LOCALAPPDATA%\Microsoft\WinGet\Packages\Gyan.FFmpeg*\*\bin\ffmpeg.exe")))[0]


def load_audio(path: Path):
    """Decode with ffmpeg (PyAV's DLL is blocked by Windows Application Control on this machine)."""
    import numpy as np
    raw = subprocess.run([ffmpeg(), "-v", "error", "-i", str(path), "-f", "f32le", "-ac", "1", "-ar", "16000", "-"],
                         capture_output=True, check=True).stdout
    return np.frombuffer(raw, dtype=np.float32)


def verify(lessons):
    """Re-transcribe each window listed in audio_checks_pending.json with small.en (beam search).

    The pipeline removes text it suspects Gemini inserted only when this second, stronger check does not
    hear its content words either. Results go to audio_checks.json (keyed by candidate)."""
    from faster_whisper import WhisperModel
    model = None
    for L in lessons:
        d = STATE / "lessons" / L["id"]
        pend_path, res_path = d / "audio_checks_pending.json", d / "audio_checks.json"
        if not pend_path.exists():
            continue
        pending = json.loads(pend_path.read_text(encoding="utf-8")) or []
        results = json.loads(res_path.read_text(encoding="utf-8")) if res_path.exists() else {}
        todo = [p for p in pending if p["key"] not in results]
        if not todo:
            continue
        if model is None:
            model = WhisperModel("small.en", device="cpu", compute_type="int8", cpu_threads=os.cpu_count() or 4)
        audio = load_audio(CACHE / L["id"] / "audio.flac")
        for p in todo:
            a, b = int(p["start"] * 16000), int(p["end"] * 16000)
            segs, _ = model.transcribe(audio[a:b], language="en", beam_size=5, condition_on_previous_text=False)
            text = " ".join(s.text.strip() for s in segs)
            results[p["key"]] = {"model": "small.en", "window": [p["start"], p["end"]], "text": text}
            print(f"check {L['id']} [{p['start']:.0f}-{p['end']:.0f}s]: heard \"{text[:100]}\"", flush=True)
        tmp = res_path.with_name(res_path.name + ".tmp")
        tmp.write_text(json.dumps(results, indent=1), encoding="utf-8")
        os.replace(tmp, res_path)


def main():
    sys.stdout.reconfigure(encoding="utf-8")
    args = sys.argv[1:]
    model_name = args[args.index("--model") + 1] if "--model" in args else "base.en"
    out_name = args[args.index("--out") + 1] if "--out" in args else "whisper_words.json"
    wanted = None
    if "--lessons" in args:
        wanted = set()
        for part in args[args.index("--lessons") + 1].split(","):
            if "-" in part:
                a, b = part.split("-")
                wanted.update(range(int(a), int(b) + 1))
            else:
                wanted.add(int(part))
    cat = json.loads((STATE / "catalog.json").read_text(encoding="utf-8"))
    lessons = [L for L in cat["lessons"] if L.get("video") and (wanted is None or L["num"] in wanted)]
    sys.modules.setdefault("av", types.ModuleType("av"))  # faster_whisper imports av at module load
    if "--verify" in args:
        verify(lessons)
        return
    from faster_whisper import WhisperModel
    model = WhisperModel(model_name, device="cpu", compute_type="int8", cpu_threads=os.cpu_count() or 4)
    for L in lessons:
        out = STATE / "lessons" / L["id"] / out_name
        if out.exists():
            continue
        audio_path = CACHE / L["id"] / "audio.flac"
        if not audio_path.exists():
            print(f"skip {L['id']}: no cached audio (run prepare)", flush=True)
            continue
        t0 = time.time()
        audio = load_audio(audio_path)
        segs, info = model.transcribe(audio, language="en", word_timestamps=True, vad_filter=False, beam_size=1,
                                      condition_on_previous_text=False)
        words = []
        for s in segs:
            for w in s.words or []:
                words.append([round(w.start, 2), round(w.end, 2), w.word.strip(), round(w.probability, 2)])
        doc = {"lesson": L["id"], "model": model_name, "duration": info.duration,
               "elapsed_s": round(time.time() - t0, 1), "words": words}
        tmp = out.with_name(out.name + ".tmp")
        tmp.write_text(json.dumps(doc), encoding="utf-8")
        os.replace(tmp, out)
        print(f"whisper {model_name} {L['id']}: {len(words)} words, {info.duration / 60:.1f} min audio in "
              f"{doc['elapsed_s'] / 60:.1f} min", flush=True)


if __name__ == "__main__":
    main()
