import sys
import os
def f(a, L = []):
    L.append(a)
    return L
print (f(1))
print (f(2))
def f1(a, L = None):
    if L is None:
        L = []
    L.append(a)
    return L
print (f1(11))
print (f1(22))
def parrot(a, b = '1', c = 12, d = 'ABC'):
    print ('a = ', a)
    print ('b = ', b)
    print ('c = ', c)
    print ('d = ', d)
parrot(a = 10, d = '123')
parrot(a = 0, c = 123456)
def cheeseshop(kind, *arguments, **keywords):
    print ('Do you have any kind', kind, '?')
    for arg in arguments:
        print arg
    keys = sorted(keywords.keys())
    for kw in keys:
        print keywords[kw]
cheeseshop('apple', 'A', 'B', 'C', 'D',
            kind0 = 'A1',
            kind1 = 'A2',
            kind2 = 'A3',
            kind3 = 'A4')
args = [1, 5]
print range(*args)
def parrot1(voltage):
    print voltage
d = {"voltage": "A"}
parrot1(**d)
def make_incre(n):
    return lambda x : x + n
f = make_incre(100)
print f(0)
print f(10)
        

