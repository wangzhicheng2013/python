import sys
x = int(raw_input("x = "))
if 0 == x % 2:
    print '%d is odd' %x
    sys.exit(0)
num = 9
sum = 0
while True:
    sum = 10 * sum + num
    if 0 == sum % x:
        print sum
        break



            


