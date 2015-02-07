#!/usr/bin/python
def find_min(values):
	smallest = None
	for value in values:
		if smallest is None or value < smallest:
			smallest = value
		return smallest
		
def find_max(values):
	biggest = None
	for value in values:
		if biggest is None or value > biggest:
			biggest = value
	return biggest
		
values=[3, 41, 12, 9, 74, 15]
print find_min(values)
print find_max(values)