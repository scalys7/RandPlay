from random import choice,uniform

CHORD_VOICES = ["EPiano"] #TODO - add all fitting chord voices



def createGroove(grooveName, timeSig):
    grooveDefinition = ""
    grooveDefinition += generateChord(timeSig) + "\n\n"
    grooveDefinition += "DefGroove %s\n\n"%(grooveName)
    return grooveDefinition

def generateChordSeq(timeSig):
    numberOfNotes = choice(range(int(timeSig/2),int(timeSig))) + 1 #TODO - fix halfs (if time sig is a float)
    possibleStarts = range(1,int(timeSig) + 1) #TODO - fix halfs (if time sig is a float)

    seq = ""
    seq += "%d %d %d;" % (1, timeSig, choice(range(60, 100)))  # We that every will box start with a note
    possibleStarts.remove(1)
    for i in range(1,numberOfNotes):
        randomStart = choice(possibleStarts)
        possibleStarts.remove(randomStart)
        seq += "%d %d %d;"%(randomStart,timeSig,choice(range(60,100)))
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

#TODO - create generateDrum generatBase generateChordSass, generateLive, generateScaly, generateMusic