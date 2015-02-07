#!/usr/bin/python
while True:
	try:
		score =float(raw_input('Enter a Score: '))
		break
	except:
		print "Bad Score."
		
if score >= 1:
	print 'wrong score'
elif score >= 0.9 and score < 1:
	print 'A'
elif score >= 0.8:
	print 'B'
elif score >= 0.7:
	print 'C'
elif score >= 0.6:
	print 'D'
else:
	print 'F'
