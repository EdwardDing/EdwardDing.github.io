#!/usr/bin/env python
import os,sys

def renamer(inputFile, outputFile, ext):
	n = 1
	for filename in os.listdir(inputFile):

		file_ext = filename.split('.')[-1]

		if file_ext in ext:
			f = open(inputFile + '/' + filename,'r')

			line = f.read()
			f2 = open(outputFile+ '/' + str(n) + '.' + file_ext,'w')
			f2.write(line)
			n = n + 1
			f.close()
			f2.close()

if __name__ == '__main__':

	print ("\n--------------------------")
	print ("Welcome to DJR Renamer")
	print ("--------------------------\n")

	inputFile = raw_input("Drag the input folder here and hit return: ")
	outputFile = raw_input("Drag the output folder here and hit return: ")
	ext_raw = raw_input("Input the file extension you want to rename automatically\nYou can input multiple extension, separated by ',' (e.g. png,jpg) : ")	

	ext = ext_raw.split(',')
	
	renamer(inputFile.rstrip(), outputFile.rstrip(), ext)

	print "Finished! Enjoy :)"