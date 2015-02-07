def computepay(hours,rate):
	if hours < 40:
		pay=hours*rate
		print "the pay is:", pay
	else:
		pay = 40 * rate + (hours-40)*1.5*rate
		print "the pay is:", pay
		
hours=raw_input("Enter worked hours:")
hours=float(hours)
rate=10
computepay(hours,rate)
