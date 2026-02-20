from ocr_module import capture_text
from voice_module import listen
from tts_module import speak
from translate_module import to_filipino

def main():
    speak("Gab AI is ready.")

    while True:
        command = listen()

        if "read" in command:
            speak("Reading text.")
            text = capture_text()
            speak(text)

        elif "translate" in command:
            speak("Reading and translating.")
            text = capture_text()
            translated = to_filipino(text)
            speak(translated)

        elif "exit" in command or "stop" in command:
            speak("Goodbye.")
            break

        else:
            speak("Command not recognized.")

if __name__ == "__main__":
    main()
