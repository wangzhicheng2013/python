import sys
def func(number):
    i = number / 100
    j = number / 10 % 10
    k = number % 10
    return i ** 3 + j ** 3 + k ** 3
for i in range(100, 1000):
    if i == func(i):
        print i

            
