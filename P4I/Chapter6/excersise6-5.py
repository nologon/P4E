#~ //~ Exercise 6.5 Take the following Python code that stores a string:'
#~ //~ str = 'X-DSPAM-Confidence: 0.8475'
#~ //~ Use find and string slicing to extract the portion of the string after the colon
#~ //~ character and then use the float function to convert the extracted string into a
#~ //~ floating point number.


#~ The operator [n:m] returns the part of the string from the "n-eth" character to the
#~ "m-eth" character, including the first but excluding the last.

str = 'X-DSPAM-Confidence: 0.8475'
collonpos = str.find(':')
print collonpos
number = str[20:]
floatnum = float(number)
print floatnum
print type(floatnum)
