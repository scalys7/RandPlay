#/bin/python

import re
import os.path

def extractor_test(exfilename, filename):
	output = open("extractions/"+exfilename,"w")
	with open("chords/"+filename, "r") as inputChords :
		for line in inputChords :
			if "showAcc(" in line :
				extract_chords(line, output)


def extract_chords(line, output):

	for chord in re.finditer(r"\"([A-Za-z0-9]+)\"", line):
		output.write(line[chord.start() + 1 :chord.end() - 1] + " ")
	
def run_though_files():
	for dirpath, dnames, files in os.walk("chords"):
		for name in files:
			str_name = str(name)
			extracted_name = str_name[3:len(str_name)-3]
			if extracted_name :
				#print extracted_name +"\n"
				extractor_test(extracted_name, str_name)

run_though_files()
