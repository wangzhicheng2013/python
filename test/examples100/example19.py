import sys
for i in range(1, 1001):
    s = 0
    L = []
    for j in range(1, i):
        if 0 == i % j:
            s += j
            L.append(j)
    if s == i:
        print "%d is perfect number" %i
        for e in L:
            print str(e),
        print
            
