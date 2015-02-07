#!/usr/bin/python
#~ Exercise 4.6
#~ Rewrite your pay computation with time-and-a-half for overtime
#~ and create a function called  computepay
#~ which takes two parameters (hours and rate ).
#~ Enter Hours: 45
#~ Enter Rate: 10
#~ Pay: 475.

def computepay(hours,rate):
	#~ hours = int(raw_input('Enter hours: '))
	#~ rate = int(raw_input('Enter Rate: '))
	

while  True:
	try:
		computepay()
#~ computepay.rate
		break
	except:
		print "Oops!  That was no valid number.  Try again..."
print computepay.hours
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
	print ('Pay: ' + str(pay));
	
computepay(40,10)


