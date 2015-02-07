#!/usr/bin/python
largest = None
print 'Before:', largest
for itervar in [3, 41, 12, 9, 74, 15, 44, 23, 400, 245, 24, 11]:
	if largest is None or itervar > largest :
		largest = itervar
	print 'Loop:', itervar, largest
print 'Largest:', largest