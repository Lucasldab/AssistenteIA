import speech_recognition as sr

r = sr.Recognizer()
r.energy_threshold = 4000

with sr.Microphone() as source:

    while True:
        audio = r.listen(source)
        
        print(r.recognize_google(audio, language='pt'))