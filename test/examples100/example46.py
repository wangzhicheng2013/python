import sys
number = int(raw_input("number = "))
if number >= 10000 or number <= -10000:
    raise ValueError("number is too big or too small...!")
t = number * number
print 'squar = %d' %t 


