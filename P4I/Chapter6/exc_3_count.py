#!/usr/in/python
def counter(word): 
	count = 0
	for letter in word:
		if letter == 'a':
			count = count  + 1
	print 'the amount of letters a is: ',  + count
word = raw_input('enter a word:')
counter(word)
	
