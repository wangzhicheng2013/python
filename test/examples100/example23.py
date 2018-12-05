import sys
for i in range(1, 5):
    for j in range(4 - i):
        print ' ',
    for j in range(2 * i - 1):
        print '*',
    print
k = 0
for i in range(3, 0, -1):
    k = k + 1
    for j in range(k):
        print ' ',
    for j in range(2 * i - 1):
        print '*',
    print



