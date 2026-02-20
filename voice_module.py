from vosk import Model, KaldiRecognizer
import pyaudio
import json

MODEL_PATH = "vosk-model-small-en-us"

model = Model(MODEL_PATH)
rec = KaldiRecognizer(model, 16000)

def listen():
    mic = pyaudio.PyAudio()
    stream = mic.open(
        format=pyaudio.paInt16,
        channels=1,
        rate=16000,
        input=True,
        frames_per_buffer=8000
    )

    print("Listening...")
    stream.start_stream()

    while True:
        data = stream.read(4000, exception_on_overflow=False)
        if rec.AcceptWaveform(data):
            result = json.loads(rec.Result())
            command = result.get("text", "")
            return command.lower()
