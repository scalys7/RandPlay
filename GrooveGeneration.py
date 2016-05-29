from random import choice,uniform

VOICES = ["5thSawWave","Accordion","AcousticBass","AgogoBells","AltoSax","Applause/Noise","Atmosphere","BagPipe","Bandoneon","Banjo","BaritoneSax","Bass&Lead","Bassoon","BirdTweet","BottleBlow","BowedGlass","BrassSection","BreathNoise","Brightness","Celesta","Cello","Charang","ChifferLead","ChoirAahs","ChurchOrgan","Clarinet","Clavinet","CleanGuitar","ContraBass","Crystal","DistortonGuitar","EchoDrops","EnglishHorn","EPiano","Fantasia","Fiddle","FingeredBass","Flute","FrenchHorn","FretlessBass","Glockenspiel","Goblins","GuitarFretNoise","GuitarHarmonics","GunShot","HaloPad","Harmonica","HarpsiChord","HelicopterBlade","Honky-TonkPiano","IceRain","JazzGuitar","Kalimba","Koto","Marimba","MelodicTom1","MetalPad","MusicBox","MutedGuitar","MutedTrumpet","NylonGuitar","Oboe","Ocarina","OrchestraHit","OrchestralHarp","Organ1","Organ2","Organ3","OverDriveGuitar","PanFlute","Piano1","Piano2","Piano3","Piccolo","PickedBass","PizzicatoString","PolySynth","Recorder","ReedOrgan","ReverseCymbal","RhodesPiano","Santur","SawWave","SeaShore","Shakuhachi","Shamisen","Shanai","Sitar","SlapBass1","SlapBass2","SlowStrings","SoloVoice","SopranoSax","SoundTrack","SpaceVoice","SquareWave","StarTheme","SteelDrums","SteelGuitar","Strings","SweepPad","SynCalliope","SynthBass1","SynthBass2","SynthBrass1","SynthBrass2","SynthDrum","SynthStrings1","SynthStrings2","SynthVox","TaikoDrum","TelephoneRing","TenorSax","Timpani","TinkleBell","TremoloStrings","Trombone","Trumpet","Tuba","TubularBells","Vibraphone","Viola","Violin","VoiceOohs","WarmPad","Whistle","WoodBlock","Xylophone"]
CHORD_VOICES = ["EPiano","Piano1","Piano2","Piano3"]
CHORD_SUS_VOICES = ["BrassSection","Brightness","Cello","ChoirAahs","ChurchOrgan","SeaShore","Strings"]

def createGroove(grooveName):
    return "DefGroove %s\n\n"%(grooveName)


def createPossibleStartsInRange(startRange,endRange):
    doublePossibleStarts = range(startRange * 2, endRange * 2 + 1)
    PossibleStarts = []
    for doublePosibleStart in doublePossibleStarts:
        PossibleStarts.append(float(doublePosibleStart)/2)
    return PossibleStarts

def generateChordSeq(timeSig):
    numberOfNotes = choice(range(int(timeSig/2),int(timeSig))) + 1
    possibleStarts = createPossibleStartsInRange(1,int(timeSig))
    seq = ""
    seq += "%d %d %d;" % (1, 1, choice(range(60, 100)))
    possibleStarts.remove(1)
    for i in range(1,numberOfNotes):
        randomStart = choice(possibleStarts)
        possibleStarts.remove(randomStart)
        seq += "%f %d %d;"%(randomStart,1,choice(range(60,100)))
    return seq

def generateChord(timeSig):
    voice = choice(CHORD_VOICES)
    octave = choice(range(4,6))
    seq = generateChordSeq(timeSig)
    chordStr = '''Begin Chord
	Voice  {VOICE}
	Volume p
	Articulate 110
	Octave {OCTAVE}
	Voicing Mode=Optimal
	Sequence {{{SEQ}}}
End'''.format(VOICE = voice, OCTAVE = octave, SEQ = seq)
    return chordStr


def generateChordSus():
    return '''Begin Chord-Sus
	Voice  {VOICE}
	Sequence {{1 1 {VOL}}}
	Voicing Mode=Optimal
	Octave 5
	Articulate 100
	Unify On
	Rvolume 10
	Volume pp
End'''.format(VOICE = choice(CHORD_SUS_VOICES), VOL = choice(range(50,70)))

#TODO - create generateDrum generatBase generateChordSass, generateLive, generateScaly, generateMusic