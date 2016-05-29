majorKeys = ['A','Bb','B','C','Db','D','Eb','E','F','Gb','G','Ab']
minorKeys = ['A','Bb','B','C','C#','D','Eb','E','F','F#','G','G#']
keys =  majorKeys + minorKeys

majorScales =  [key +' major' for key in majorKeys]
minorScales = [key +' minor' for key in minorKeys]
scales = majorScales + minorScales

majorKeyBaseChords = ["I", "ii", "iii", "IV", "V", "vi", "vii0"]
minorKeyBaseChords = ["i", "ii0", "III", "iv", "V", "VI", "VII"]

majTable = {'C': ('C', 'D', 'E', 'F', 'G', 'A', 'B'),
            'C#': ('C#', 'D#', 'E#', 'F#', 'G#', 'A#', 'C'),
            'D': ('D', 'E', 'F#', 'G', 'A', 'B', 'C#'),
            'Db': ('Db', 'Eb', 'F', 'Gb', 'Ab', 'Bb', 'C'),
            'D#': ('D#', 'F', 'G', 'G#', 'A#', 'C', 'D'),
            'Eb': ('Eb', 'F', 'G', 'Ab', 'Bb', 'C', 'D'),
            'E': ('E', 'F#', 'G#', 'A', 'B', 'C#', 'D#'),
            'F': ('F', 'G', 'A', 'Bb', 'C', 'D', 'E'),
            'F#': ('F#', 'G#', 'A#', 'B', 'C#', 'D#', 'F'),
            'Gb': ('Gb', 'Ab', 'Bb', 'B', 'Db', 'Eb', 'F'),
            'G': ('G', 'A', 'B', 'C', 'D', 'E', 'F#'),
            'G#': ('G#', 'A#', 'C', 'C#', 'D#', 'F', 'G'),
            'Ab': ('Ab', 'Bb', 'C', 'Db', 'Eb', 'F', 'G'),
            'A': ('A', 'B', 'C#', 'D', 'E', 'F#', 'G#'),
            'A#': ('A#', 'C', 'D', 'D#', 'F', 'G', 'A'),
            'Bb': ('Bb', 'C', 'D', 'Eb', 'F', 'G', 'A'),
            'B': ('B', 'C#', 'D#', 'E', 'F#', 'G#', 'A#')}

minTable = {'C': ('C', 'D', 'Eb', 'F', 'G', 'Ab', 'Bb'),
            'C#': ('C#', 'D#', 'E', 'F#', 'G#', 'A', 'B'),
            'Db': ('Db', 'Eb', 'E', 'Gb', 'Ab', 'A', 'B'),
            'D': ('D', 'E', 'F', 'G', 'A', 'Bb', 'C'),
            'D#': ('D#', 'F', 'F#', 'G#', 'A#', 'B', 'C#'),
            'Eb': ('Eb', 'F', 'Gb', 'Ab', 'Bb', 'B', 'Db'),
            'E': ('E', 'F#', 'G', 'A', 'B', 'C', 'D'),
            'F': ('F', 'G', 'Ab', 'Bb', 'C', 'Db', 'Eb'),
            'F#': ('F#', 'G#', 'A', 'B', 'C#', 'D', 'E'),
            'Gb': ('Gb', 'Ab', 'A', 'B', 'Db', 'D', 'E'),
            'G': ('G', 'A', 'A#', 'C', 'D', 'D#', 'F'),
            'G#': ('G#', 'A#', 'B', 'C#', 'D#', 'E', 'F#'),
            'Ab': ('Ab', 'Bb', 'B', 'Db', 'Eb', 'E', 'Gb'),
            'A': ('A', 'B', 'C', 'D', 'E', 'F', 'G'),
            'A#': ('A#', 'C', 'C#', 'D#', 'F', 'F#', 'G#'),
            'Bb': ('Bb', 'C', 'Db', 'Eb', 'F', 'Gb', 'Ab'),
            'B': ('B', 'C#', 'D', 'E', 'F#', 'G', 'A')}
#TODO: add double #/b?
enharmonics = {
    "A#":"Bb",
    "B#":"C",
    "C#":"Db",
    "D#":"Eb",
    "E#":"Fb",
    "F#":"Gb",
    "G#":"Ab",

    "Bb": "A#",
    "C" : "B#",
    "Db" : "C#",
    "Eb" : "D#",
    "Fb" : "E#",
    "Gb": "F#",
    "Ab" : "G#",
}

def key(scale):
    return scale.split(' ')[0]


def relativeScale(scale):
    if(isMinor(scale)):
        return majorKeys[(minorKeys.index(key(scale)) + 3) % len(minorKeys)] + " major"
    else:
        return minorKeys[(majorKeys.index(key(scale)) + 9) % len(majorKeys)] + " minor"

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