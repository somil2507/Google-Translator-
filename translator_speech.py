import googletrans
import speech_recognition as sr
import gtts
import playsound

r = sr.Recognizer()
with sr.Microphone() as source:
    print("Speak Now")
    voice = r.listen(source)
    text = r.recognize_google(voice, language='en')
    print(text)


translator = googletrans.Translator()

translation = translator.translate(text, dest='hi')
print(translation.text)
converted_audio = gtts.gTTS(translation.text, lang='hi')
converted_audio.save("hello.mp3")
playsound.playsound("hello.mp3")


#print(googletrans.LANGUAGES)