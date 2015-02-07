#!/usr/bin/python
celcius = raw_input('What is the temperature in Celcius? ')
try:
	fahrenheit = float(celcius) * 9/5 + 32
	print ('the temperature in Fahrenheit is: ' + str(fahrenheit) + ' fahrenheit')
except:
	print 'numbers motherfucker!'
	
