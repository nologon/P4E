#!/usr/bin/python
def greet(lang):
	if lang == 'es':
		print 'Hola'
	if lang == 'en':
		print 'Hello'
	if lang == 'fr':
		print 'Bonjour'
		
lang = raw_input('Select Language: en, fr, es: ')
greet(lang)