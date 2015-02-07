#!/usr/bin/python

def greet(lang):
	if lang == 'es':
		return 'Hola'
	if lang == 'fr':
		return 'Bonjour'
	else:
		return 'Hello'
		
#~ def greet():
	#~ return "Hello"
	
print greet('en'),'Glenn'
print greet('es'),"Sally"