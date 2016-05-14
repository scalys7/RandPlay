from random import randint,choice
from os import listdir
from os.path import isfile, join
import os
#keys = ['A','A#','B','C','C#','D','D#','E','F','F#','G','G#']
keys = ['A','B','C','D','E','F','G'] #TODO: why are # causing a problem?
majorKeyChords = ["I","ii","iii","IV","V7","vi","vii0"]
grooves = [f.split('.')[0] for f in listdir('''C:\MMA\Lib\stdlib''') if isfile(join('''C:\MMA\Lib\stdlib''', f)) and f.endswith('mma')]

f = file('out.mma','w')

def write(line):
    f.writelines(line + '\n')

tempo = randint(60,150)
key = choice(keys)

write("tempo "+str(tempo))

write("KeySig "+ key)
write("Time 4")
write("")
write("Groove Metronome2-4")

write("")
write("")

for i in range(0,2):
    write("Groove " + choice(grooves))
    write('\t'+'I') #start chord progression with tonic
    for j in range(1,3):
        write("\t"+choice(majorKeyChords))
    write("\t" + choice(["V7",'vii0'])) #end with dominant

write('\t' + 'I')  # end song with tonic

f.close()

os.system("out.mma")
os.system("out.mid")
