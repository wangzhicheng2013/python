import sys
L = []
for i in range(10):
    L.append(int(raw_input("element = ")))
print L
maxIndex = L.index(max(L))
minIndex = L.index(min(L))
L[0], L[maxIndex] = L[maxIndex], L[0]
L[len(L) - 1], L[minIndex] = L[minIndex], L[len(L) - 1]
print L
