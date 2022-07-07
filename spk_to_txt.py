#!/usr/env/bin python
import speech_recognition 
from requests import delete
import csv

r = speech_recognition.Recognizer()

while True:
    print("..Count: 1,2,3 (in your head) then Speak:--")
    with speech_recognition.Microphone() as source:
        r.adjust_for_ambient_noise(source, duration=1)
        audio = r.listen(source)

        text = r.recognize_google(audio)
        print(f"I Heard you say:  {text}")

        with open ("spk_to_txt_inputs.txt", "a") as f:
            f.write(text + '\n')

    if "exit" in text:
        exit()
    else:
        continue

