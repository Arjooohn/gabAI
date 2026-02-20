import pyttsx3

engine = pyttsx3.init()

def speak(text):
    if not text:
        text = "No text detected."
    print("GabAI:", text)
    engine.say(text)
    engine.runAndWait()
