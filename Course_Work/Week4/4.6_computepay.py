__author__ = 'thijn'
# 4.6 Write a program to prompt the user for hours and rate per hour using raw_input to compute gross pay.
# Award time-and-a-half for the hourly rate for all hours worked above 40 hours.
# Put the logic to do the computation of time-and-a-half in a function called computepay()
# and use the function to do the computation. The function should return a value.
# Use 45 hours and a rate of 10.50 per hour to test the program (the pay should be 498.75).
# You should use raw_input to read a string and float() to convert the string to a number.
# Do not worry about error checking the user input unless you want to - you can assume the user types numbers properly.
hours = 40
pay = 0
def computepay(h,r):
    if h > 40:
        overtime = h  - hours
        pay = (hours * r) + (overtime * (r * 1.5))
        return pay
        #return 42.37
    elif h <= 40:
        h = h * rate
        return h

hrs = raw_input("Enter Hours:")
hrs = int(hrs)
rate  = raw_input("Enter Rate:")
rate = float(rate)
p = computepay(hrs,rate)
print "Pay",p