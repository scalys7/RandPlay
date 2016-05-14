from random import randint,choice
from os import listdir
from os.path import isfile, join
import os
from MusicalNotation import *
from ChordProgression import generateClassicChordsProgression


grooves = [f.split('.')[0] for f in listdir('''C:\MMA\Lib\stdlib''') if isfile(join('''C:\MMA\Lib\stdlib''', f)) and f.endswith('mma')]

f = file('out.mma','w')

def write(line):
    f.writelines(line + '\n')

def printChordProgression(chords):
    for chord in chords:
        write('\t'+chord)

tempo = randint(60,150)
key = choice(scales)


write("tempo "+str(tempo))
write("KeySig "+ key)
write("Time "+ str(choice(timeSignatures)))
write("")
write("Groove Metronome2-4")

write("")
write("")

for i in range(0,2):
    write("Groove " + choice(grooves))
    printChordProgression(generateClassicChordsProgression(key,3))

write('\t' + tonic(key))  # end song with tonic

f.close()

os.system("out.mma")
os.system("out.mid")
