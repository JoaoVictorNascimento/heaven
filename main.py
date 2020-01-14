#!/usr/bin/env python
# -*- coding: utf-8 -*- 
import speech_recognition as sr
from gtts import gTTS
import os
import time
import playsound

def speak(text):
    tts = gTTS(text=text, lang='pt-br')
    filename = 'voice.mp3'
    tts.save(filename)
    playsound.playsound(filename)


def get_audio():
    r = sr.Recognizer()
    
    with sr.Microphone() as source:
        audio = r.listen(source)
        said = ""
        
        try:
            said = r.recognize_google(audio)
            print(said)
        except Exception as ex:
            print("Exception: " + str(ex))
    
    return said
            
     
speak("Olá, eu sou a Heaven")
get_audio()