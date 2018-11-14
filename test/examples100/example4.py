import sys
year = int(raw_input("year = "))
month = int(raw_input("month = "))
day = int(raw_input("day = "))
months = (0,31,59,90,120,151,181,212,243,273,304,334)
if month > 0 and month <= 12:
    total = months[month - 1] + day
else:
    raise TypeError("month is invalid...!") 
if (0 == year % 400) or ((0 == year % 4) and (year % 100 != 0)):
    if (month > 2):
        total += 1
print 'it is the %dth days' %total
    




