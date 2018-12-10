import sys
def fun(n):
    if n <= 0:
        return 0
    elif 1 == n:
        return 1
    else:
        return n * fun(n - 1)
print fun(5)
print fun(-120)
    
