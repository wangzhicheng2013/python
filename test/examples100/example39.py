import sys
L = [1, 3, 5, 10, 12]
x = int(raw_input("x = "))
L.append(x)
for i in range(len(L) - 2, -1, -1):
    if L[i] > x:
        L[i + 1] = L[i]
L[i + 1] = x
for i in range(len(L)):
    print L[i]
