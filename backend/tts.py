import asyncio
import edge_tts
import sounddevice as sd
import soundfile as sf
import threading

async def speak_async(text, lang):
    voice = "hi-IN-SwaraNeural" if lang == "hi" else "en-IN-NeerjaExpressiveNeural"
    file = "static/output.wav"

    communicate = edge_tts.Communicate(text, voice)
    await communicate.save(file)

    data, sr = sf.read(file)
    sd.play(data, sr)
    sd.wait()

def _run_async(text, lang):
    asyncio.run(speak_async(text, lang))

def speak(text, lang="en"):
    threading.Thread(
        target=_run_async,
        args=(text, lang),
        daemon=True
    ).start()