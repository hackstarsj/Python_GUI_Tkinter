import speech_recognition as sr

# get audio from the microphone
audio_text=""
r = sr.Recognizer()
with sr.Microphone() as source:
    print("Speak:")
    audio = r.listen(source)

try:
    audio_text=r.recognize_google(audio)
    print("You said " + audio_text)
except sr.UnknownValueError:
    print("Could not understand audio")
except sr.RequestError as e:
    print("Could not request results; {0}".format(e))

#
# text to speech
from gtts import gTTS

# This module is imported so that we can
# play the converted audio
import os

# The text that you want to convert to audio
mytext = audio_text

# Language in which you want to convert
language = 'en'

# Passing the text and language to the engine,
# here we have marked slow=False. Which tells
# the module that the converted audio should
# have a high speed
myobj = gTTS(text=mytext, lang=language, slow=False)

# Saving the converted audio in a mp3 file named
# welcome
myobj.save("welcome.mp3")

# Playing the converted file
from playsound import playsound
playsound('demo.mp3')



import pygame
from time import sleep
pygame.mixer.init()
pygame.mixer.music.load(open("demo.mp3","rb"))
print("")
pygame.mixer.music.play()
while pygame.mixer.music.get_busy():
    pass
    #print("Playing")
    #sleep(1)
print("done")

