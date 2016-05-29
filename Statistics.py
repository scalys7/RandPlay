import os
from os.path import isfile, join
from MusicalNotation import *
from ChordProgression import *
from collections import Counter
from itertools import groupby

def extractChords(band = 'Coldplay'):
    fileContents = [file(join("chords", f)).read() for f in os.listdir("chords") if isfile(join("chords", f)) and band in f]
    chordsList = map(lambda x: x.split(' '), fileContents)
    return [chords for chords in chordsList if len(chords) > 20 and chords[0]==chords[-2]]


def extractAllChordProgressions():
    chordsList = extractChords()
    scales = map(lambda x: inferScale(x), chordsList)
    chordProgressions = map(extractRomanChordProgressions, chordsList)
    return reduce(lambda x, y: x + y, chordProgressions)

def commonProgression(minLength = 2):
    chordProgressions = filter(lambda x: len(x)>=minLength,extractAllChordProgressions())
    return max(groupby(sorted(chordProgressions)), key=lambda(x, v):(len(list(v)),-chordProgressions.index(x)))[0]


print commonProgression(3)
