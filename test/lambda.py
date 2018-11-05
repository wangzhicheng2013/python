import sys
from collections import deque
def make_incre(n):
    return lambda x : x + n
f = make_incre(100)
print f(100)
print f(200)
pairs = [("C", 110), ("A", 0), ("E", 12)]
print pairs
pairs.sort(key = lambda pair : pair[1])
print pairs

def func():
    '''
        noting to do
    '''
    pass
print func.__doc__

def func1(a, b):
    print a, b
func1(10, 20)
L = ["A", "B"]
L.append("C")
print L
LL1 = L
print LL1
LL1.append(L)
for l in LL1:
    print l
A = [1, 2, 0.112, 1212]
print A.count(2)
A.insert(0, -100.1)
print A
A.reverse()
print A
print A.pop()
myqueue = deque(L)
print myqueue
myqueue.append("Hello world...!")
print myqueue
