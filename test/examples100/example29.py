import sys
def fun(n):
    num = 0
    while n > 0:
        print n % 10
        n = n / 10
        num = num + 1
    return num
print "num = {0}".format(fun(123456))
