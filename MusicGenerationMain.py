from random import randint,choice
from os import listdir
from os.path import isfile, join
import os
from MusicalNotation import *
from ChordProgression import generateClassicChordsProgression
from GrooveGeneration import *

f = file('out.mma','w')

def write(line):
    f.writelines(line + '\n')

def writeChordProgression(chords, numChordsInBar = 1):

    for i in range(0,len(chords)/numChordsInBar):
        write('\t'+ reduce(lambda x,y: x+" "+y, chords[i:i+numChordsInBar]))

    if(len(chords)%numChordsInBar!=0):
        write('\t' + reduce(lambda x, y: x + " " + y,
                        chords[(len(chords)/numChordsInBar)*numChordsInBar:]))


tempo = randint(60,150)
scale = choice(scales)
timeSig = choice(timeSignatures)

#write("tempo "+str(tempo))
#write("KeySig " + scale)
write("Time "+ str(timeSig))
write("")
#write("Groove Metronome2-4")

write("")
write("")

aPartGroove = generateChord(timeSig)
write(aPartGroove)
write(createGroove("APart"))
write('groove %s\n\n'%("APart"))
write("KeySig " + scale)
writeChordProgression(list(generateClassicChordsProgression(scale, 3)))

#transition into course

#write("SeqClear") This is
write(generateChordSus())
write(createGroove("BPart"))
write('groove %s\n\n'%("BPart"))
write("tempo "+str(int(tempo*1.1)))
write("KeySig " + relativeScale(scale))
writeChordProgression(list(generateClassicChordsProgression(scale, 3)))



write('groove %s\n\n'%("APart"))
write("tempo "+str(int(tempo*0.9)))
write("KeySig " + scale)
writeChordProgression(list(generateClassicChordsProgression(scale, 3)))

write('\t' + tonic(scale))  # end song with tonic

f.close()

try :
    os.remove("out.mid")
except:
    pass

os.system("out.mma")
os.system("out.mid")
