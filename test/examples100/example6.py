import sys
def fib(n):
    if (n < 0):
        raise TypeError("argument invalid...!")
    if (0 == n):
        return 0
    elif (1 == n):
        return 1
    else:
        a, b = 0, 1
        for i in range(n - 1):
            a, b = b, a + b
    return b
print fib(2)
print fib(9)



