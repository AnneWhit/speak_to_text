from requests import delete
import speech_recognition as sr
import time
import csv

r = sr.Recognizer()

def speak():
    with sr.Microphone() as source:
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)
        voice_data = ''
        try:
            voice_data = r.recognize_google(audio)
        except sr.UnknownValueError:
            print('Sorry, I did not get that')
        except sr.RequestError:
            print('Sorry, my speech service is down')
        return voice_data


time.sleep(1)
while 1:
    voice_data = speak()
    if 'exit' in voice_data:
        exit()
    print(voice_data, end='\n')
    with open ('text.txt','a') as f:
        f.write(voice_data)
    #if 'exit now' in voice_data:
    #    exit()

