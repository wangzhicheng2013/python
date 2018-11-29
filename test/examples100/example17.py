import sys
import string
s = raw_input("input a string = ")
letters = 0
space = 0
digit = 0
others = 0
for ch in s:
    print ch
    if ch.isalpha():
        letters += 1
    elif ch.isspace():
        space += 1
    elif ch.isdigit():
        digit += 1
    else:
        others += 1
print 'letters number = %d' %letters
print 'space number = %d' %space
print 'digit number = %d' %digit
print 'others number = %d' %others

            
