from random import randint,choice
from os import listdir
from os.path import isfile, join
import os
keys = ['A','A#','B','C','C#','D','D#','E','F','F#','G','G#']

grooves = [f.split('.')[0] for f in listdir('''C:\MMA\Lib\stdlib''') if isfile(join('''C:\MMA\Lib\stdlib''', f)) and f.endswith('mma')]

f = file('out.mma','w')

def write(line):
    f.writelines(line + '\n')

tempo = randint(60,150)
key = choice(keys)

write("tempo "+str(tempo))

write("Keysig "+ key)
write("")
write("Groove Metronome2-4")

write("")
write("")

for i in range(0,2):
    write("Groove " + choice(grooves))
    for j in range(1,5):
        write("\t"+choice(keys))


f.close()

os.system("out.mma")
os.system("out.mid")