import sys
try:
    origin = int(raw_input("raw num = "))
except ValueError, e:
    print e
finally:
    L = []
    while origin > 0:
        L.append(origin % 10)
        origin = origin / 10
    L.reverse()
    print L
    for i in range(len(L)):
        L[i] = L[i] + 5
        L[i] = L[i] % 10
    print L
    L[0], L[3] = L[3], L[0]
    L[1], L[2] = L[2], L[1]
    print L
    sum = 0
    for i in range(len(L)):
        sum = sum * 10 + L[i]
    print sum



            



