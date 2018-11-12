import sys
for i in range(1, 85):
    if 0 == 168 % i:
        j = 168 / i
        if i > j and 0 == (i + j) % 2 and 0 == (i - j) % 2:
            m = (i + j) / 2
            n = (i - j) / 2
            x = n * n - 100
            print x

