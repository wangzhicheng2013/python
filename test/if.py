import sys
x = int(input("x = "))
if x < 0:
    print 'x < 0'
elif x == 0:
    print 'x == 0'
else:
    print 'x > 0'
words = ['1', '2', '300']
for word in words:
    print word
for word in words[:]:
    if len(word) > 2:
        words.insert(0, word)
print words
for i in range(10):
    print i
for i in range(1, 100, 20):
    print i
print range(100)
mylist = list(range(10))
print mylist
for n in range(2, 100):
    for i in range(2, n):
        if 0 == n % i:
            print n, ' = ', i, '*', n / i
            break
    else:
        print n, ' is a prime'
        continue
def fib(n):
    result = []
    a, b = 0, 1
    while a < n:
        result.append(a)
        a, b = b, a + b
    return result
fun = fib
result = fun(10)
print result
