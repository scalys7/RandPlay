from MusicalNotation import *
from random import choice
from Helper import group

'''
    Generates a chord progression in the following form:
    [tonic][pre-dominant]*numChords[dominant]
'''
def generateClassicChordsProgression(key,numChords = 4):
    yield scaleChords(key)[0]

    for i in range(0,numChords):
        yield choice(predominantChords(key))

    yield choice(dominantChords(key))

def englishChordToRoman(chord, scale):
    chordKey = inferChordKey(chord)
    baseChords,table,keysOfScale = (minorKeyBaseChords,minTable,minorKeys) if(isMinor(scale)) \
                            else (majorKeyBaseChords,majTable,majorKeys)

    try:
        index = table[key(scale)].index(chordKey)
        return baseChords[index]
    except: pass
    try:
        index = table[key(scale)].index(keysOfScale[keysOfScale.index(chordKey) - 1])
        return baseChords[index] + "#"
    except: pass

    try:
        index = table[key(scale)].index(keysOfScale[keysOfScale.index(chordKey) + 1])
        return baseChords[index] + "b"
    except: pass
    index = table[key(scale)].index(enharmonics[keysOfScale[keysOfScale.index(chordKey) + 1]])
    return baseChords[index] + "b"



def inferTonic(chords):
    return chords[0] #assume song is in classic formation and starts with a tonic


def inferChordKey(chord):
    return max([k for k in keys if chord.startswith(k)],key=len)

def inferKey(chords):
    tonic = inferTonic(chords)
    return inferChordKey(tonic)

def inferScale(chords):
    tonic = inferTonic(chords)
    key = inferChordKey(tonic)
    scale = key + (' minor' if(tonic.endswith('m') or tonic.endswith('min') or tonic.endswith('minor'))
        else ' major')

    return scale

def extractAbsoluteChordsProgressions(chords):
    tonic = inferTonic(chords)
    return filter(lambda x: len(x) > 1,list(group(chords, tonic)))

#extract chord progressions relative to a scale
def extractRomanChordProgressions(chords):
    scale = inferScale(chords)
    englishProgressions = extractAbsoluteChordsProgressions(chords)
    return map(lambda y: map(lambda x: englishChordToRoman(x,scale),y), englishProgressions)


