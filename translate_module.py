from googletrans import Translator

translator = Translator()

def to_filipino(text):
    try:
        translated = translator.translate(text, dest="tl")
        return translated.text
    except:
        return "Translation error."
