#!/usr/bin/python
count = 0
total = 0
num_list = []
while True:
	inp = (raw_input('Enter a number: '))

	# Handle edge case
	if inp == 'done' : break
	if len(inp) < 1 : break			#check for empty  line
	num_list.append(inp)
	# Do the work
	try :
		num = float(inp)
	except: 
		print "Invalid input"
		continue
	#~ count = count + 1
	#~ total = total + num
	#~ print num, total, count

#~ print num_list
print min(num_list)
print max(num_list)
#~ print 'Count = ', count
#~ print 'Average:', total / count