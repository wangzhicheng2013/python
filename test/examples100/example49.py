import sys
MAXNUM = lambda x, y : (x > y) * x + (x < y) * y
MINNUM = lambda x, y : (x > y) * y + (x < y) * x
a = 10
b = 20
print 'larger number = %d' %MAXNUM(a, b)
print 'small number = %d' %MINNUM(a, b)
