import speech_recognition as sr
from time import ctime
import webbrowser as wb
import pyaudio
import pywhatkit
import time
from gtts import gTTS
import playsound
import os
import random


r = sr.Recognizer()

def record_audio(ask=False):
    with sr.Microphone() as source:
        #if ask:
        #    print(ask)
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)
        voice_data = ''
        try:
            voice_data = r.recognize_google(audio)
        except sr.UnknownValueError:
            isabella_speak('Sorry, I did not get that')
        except sr.RequestError:
            isabella_speak('Sorry, my speech service is down')
        # Need to add InternetException to excepts
        
        return voice_data
 
def isabella_speak(audio_string):
    tts = gTTS(text=audio_string,lang='en')
    ran = random.randint(1,1000000)
    audio_file = 'audio-' + str(ran) + '.mp3'
    tts.save(audio_file)
    playsound.playsound(audio_file)
    print(audio_string)
    os.remove(audio_file)

def respond(voice_data):
    if 'what is your name' in voice_data:
        isabella_speak('My name is Isabella')
    elif 'what time is it' in voice_data:
        isabella_speak(ctime())
    elif 'search' in voice_data:
        #search = record_audio('What do you want to search for?')
        isabella_speak('Hold on, I will find ' + voice_data)
        pywhatkit.search(voice_data)
        #wb.register('chrome', None)
        #wb.open("https://www.google.com/search?q=" + voice_data)
        #url = 'https://google.com/search?q=' + search
        #wb.open(url)
        #print('Here is what I found for ' + search)
    elif 'youtube' or 'find' in voice_data:
        isabella_speak('I bring that up on youtube  ' + voice_data)
        pywhatkit.playonyt(voice_data)
    # if 'maps' in voice_data:
    #     #print('Where would you like to see on maps')
    #     maps=''
    #     maps = record_audio("What location")
    #     wb.open('https://www.google.com/maps/search/ ' + maps)
    elif 'exit' in voice_data:
        exit()
    

time.sleep(1)
isabella_speak('How can I help you?')
while 1:
    voice_data = record_audio()
    respond(voice_data)
