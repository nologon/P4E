#!/usr/bin/env python

#~ Exercise 7.1 Write a program to read through a file and print the contents of the
#~ file (line by line) all in upper case. Executing the program will look as follows:
file = 'mbox-short.txt'
#~ file = raw_input('what is the filename?: ')
file_opened = open(file)
for line in file_opened:
	line = line.rstrip()
	print line

