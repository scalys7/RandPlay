keys = ['A','A#','B','C','C#','D','D#','E','F','F#','G','G#']
majorScales =  [key +' major' for key in keys]
minorScales = [key +' minor' for key in keys]
scales = majorScales + minorScales

majorKeyBaseChords = ["I", "ii", "iii", "IV", "V7", "vi", "vii0"]
minorKeyBaseChords = ["i", "ii0", "III", "iv", "V7", "VI", "VII"]



def isMinor(scale):
    return scale.endswith('minor')

def scaleChords(scale):
    return majorKeyBaseChords if (not isMinor(scale)) else minorKeyBaseChords

def dominantChords(scale):
    chords = scaleChords(scale)
    if(isMinor(scale)):
        return [chords[1],chords[4]]
    else:
        return [chords[4],chords[6]]

def predominantChords(scale):
    chords = scaleChords(scale)
    return [chords[1],chords[3]]

def tonic(scale):
    return scaleChords(scale)[0]
timeSignatures = [2,3,4,5/2.0,7/2.0] #in quarter notes