from random import choice,uniform

CHORD_VOICES = ["EPiano"]



def createGroove(grooveName, timeSig):
    grooveDefinition = ""
    grooveDefinition += generateChord(timeSig) + "\n\n"
    grooveDefinition += "DefGroove %s\n\n"%(grooveName)
    return grooveDefinition

def generateChordSeq(timeSig):
    numberOfNotes = choice(range(int(timeSig/2),int(timeSig))) + 1
    possibleStarts = range(0,int(timeSig)) #TODO - fix halfs
    seq = ""
    for i in range(0,numberOfNotes):
        randomStart = choice(possibleStarts)
        possibleStarts.remove(randomStart)
        seq += "%d %d %d;"%(randomStart,choice(range(1,3)),choice(range(60,100)))
    return seq

def generateChord(timeSig):
    voice = choice(CHORD_VOICES)
    octave = choice(range(4,9))
    seq = generateChordSeq(timeSig)
    groveString = '''Begin Chord
	Voice  {VOICE}
	Volume p
	Articulate 110
	Octave {OCTAVE}
	Voicing Mode=Optimal
	Sequence {{{SEQ}}}
End'''.format(VOICE = voice, OCTAVE = octave, SEQ = seq)
    return groveString