#!/usr/bin/python
from os import system, mkdir

path = 'synth-sounds/'
voice = 'Alex'
rate = 250
wordList = [
    "hello",
    "goodbye",
    "yesterday",
    "one fine day"]

mkdir(path)
for word in wordList :
    system("say -v"+voice+" -r "+rate+" "+word+" -o "+path+word+".wav " +"--data-format=LEF32@32000")
