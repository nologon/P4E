#!/usr/bin/python
while True:
	try:
		hours = int(raw_input('Enter hours: '))
		rate = int(raw_input('Enter Rate: '))
		break
	except:
		print "Oops!  That was no valid number.  Try again..."
basehours = 40
if hours > 40:
	overtime = hours - basehours	#overtime - hours
	basepay = basehours * rate
	overtime_pay = overtime * rate * 1.5
	new_pay = float(hours) + overtime
	print ('Pay: ' + str(basepay + overtime_pay))
else:
	if hours <=40:
		print 'less than 40 hrs'
		pay = hours * rate
	print ('Pay: ' + str(pay))

