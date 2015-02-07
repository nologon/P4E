data = 'From stephen.marquard@uct.ac.za Sat Jan 09:14:16 2008'
#~ data = 'X-DSPAM-Confidence: 0.8475'
atpos = data.find('@')
#~ print atpos
sppos = data.find(' ',atpos)
#~ sppos = data.find(' ',atpos)
print sppos
host = data[atpos+1:sppos]
print host