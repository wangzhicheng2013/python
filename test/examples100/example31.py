import sys
letter = raw_input("letter = ")
if 'S' == letter:
    print 'input the second letter = '
    letter = raw_input("letter = ")
    if 'a' == letter:
        print 'Saturday'
    elif 'u' == letter:
        print 'Sunday'
    else:
        print 'input error...!'
elif 'F' == letter:
    print 'Friday'
elif 'M' == letter:
    print 'Monday'
elif 'T' == letter:
    print 'input the second letter = '
    letter = raw_input("letter = ")
    if 'u' == letter:
        print 'Tuesday'
    elif 'h' == letter:
        print 'Thursday'
    else:
        print 'input error...!'
elif 'W' == letter:
    print 'Wednesday'
else:
    print 'input error...!'

