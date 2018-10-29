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
