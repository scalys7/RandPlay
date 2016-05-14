from MusicalNotation import *
from random import choice

'''
    Generates a chord progression in the following form:
    [tonic][pre-dominant]*numChords[dominant]
'''
def generateClassicChordsProgression(key,numChords = 4):
    yield scaleChords(key)[0]

    for i in range(0,numChords):
        yield choice(predominantChords(key))

    yield choice(dominantChords(key))