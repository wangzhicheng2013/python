import sys
def fun(n):
    if 0 == n % 2:
        return funOdd(n)
    else:
        return funEven(n)
def funOdd(n):
    sum = 0
    for i in range(2, n + 1, 2):
        sum = sum + 1.00 / i
    return sum
def funEven(n):
    sum = 0
    for i in range(1, n + 1, 2):
        sum = sum + 1.00 / i
    return sum
print fun(6)
