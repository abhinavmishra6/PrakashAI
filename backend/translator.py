from mtranslate import translate

def to_english(text):
    try:
        a=translate(text, "en")
        print("Prakash listens: ",a)
        return a
    except Exception as e:
        print("Translation error:", e)
        return text
def to_hindi(text):
    try:
        a = translate(text, "hi")
        print("Prakash Said (Hindi):", a)
        return a
    except Exception as e:
        print("Translation error:", e)
        return text