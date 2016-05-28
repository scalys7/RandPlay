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

def printChordProgression(chords, numChordsInBar = 1):

    for i in range(0,len(chords)/numChordsInBar):
        write('\t'+ reduce(lambda x,y: x+" "+y, chords[i:i+numChordsInBar]))

    if(len(chords)%numChordsInBar!=0):
        write('\t' + reduce(lambda x, y: x + " " + y,
                        chords[(len(chords)/numChordsInBar)*numChordsInBar:]))


tempo = randint(60,150)
scale = choice(scales)


#write("tempo "+str(tempo))
#write("KeySig " + scale)
timeSig = choice(timeSignatures)
write("Time "+ str(timeSig))
write("")
#write("Groove Metronome2-4")

write("")
write("")
grooveName = "simpleGroove"
write(createGroove(grooveName, timeSig))
write('groove %s\n\n'%(grooveName))
write("KeySig " + scale)

printChordProgression(list(generateClassicChordsProgression(scale, 3)),2)

#transition into course
write("tempo "+str(int(tempo*1.1)))
write("KeySig " + relativeScale(scale))
#change groove?
printChordProgression(list(generateClassicChordsProgression(scale, 3)),4)

#slow ending
write("tempo "+str(int(tempo*0.9)))
write("KeySig " + scale)
printChordProgression(list(generateClassicChordsProgression(scale, 3)), 1)

write('\t' + tonic(scale))  # end song with tonic

f.close()

try :
    os.remove("out.mid")
except:
    pass

os.system("out.mma")
os.system("out.mid")
