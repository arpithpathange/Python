#!/usr/bin/python

import os

text = "speak to me"
tts_text = text.replace(" ","+")
tts_url = "http://translate.google.com/translate_tts?tl=en&q="+tts_text
os.system("wget tts_url -O test.mp3")
os.system("aplay test.mp3")
