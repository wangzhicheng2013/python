import sys
def fun(n):
    if n <= 0 or not isinstance(n, int):
        print '%d is not postive integer' %n
        return
    if 1 == n:
        print 'n = %d' % n
        return
    print 'n = ',
    while n > 1:
        for index in range(2, n + 1):
            if 0 == (n % index):
                n /= index
                if 1 == n:
                    print index,
                else:
                    print '{} *'.format(index),
                break
    print '* 1' 
fun(2)
fun(5)
fun(50)
fun(4)

            
