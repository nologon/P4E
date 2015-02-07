#!/usr/bin/python

#~ Exercise 7.2 Write a program to prompt for a file name, and then read through
#~ the file and look for lines of the form:
#~ X-DSPAM-Confidence: 0.8475
#~ When you encounter a line that starts with "X-DSPAM-Confidence:" pull apart
#~ the line to extract the floating point number on the line. Count these lines and the
#~ compute the total of the spam confidence values from these lines. When you reach
#~ the end of the file, print out the average spam confidence.
#~ Enter the file name: mbox.txt
#~ Average spam confidence: 0.894128046745
#~ Enter the file name: mbox-short.txt
#~ Average spam confidence: 0.750718518519
#~ Test your file on the mbox.txt and mbox-short.txt files.
count = 0
total = 0
#~ str = 'X-DSPAM-Confidence: 0.8475'
str = 'X-DSPAM-Confidence:'
#~ file = raw_input('Filename please: ')
#~ file = 'mbox-short.txt'
file = 'mbox.txt'
file_opened = open(file)
for line in file_opened:
	line = line.rstrip()
	if line.startswith(str) :
		count = count + 1
		#~ 	print line
		#~ print line
		#~ for line in line:
		#~ print line
		cpos = line.find(':')
		#~ print cpos
		number = line[20:]
		floatnum = float(number)
		avg = total + floatnum
		print avg
		#~ print type(floatnum)
		
print 'I counted %d lines with that matched ' % count
#~ print floatnum
		
		
	#~ if line.find(str) == -1 :
		#~ continue
	#~ print line







