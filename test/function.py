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

