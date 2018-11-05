import sys
from math import pi
L = []
for index in range(10):
    L.append(index * index)
print L
L1 = list(map(lambda x : x ** 2, range(10)))
print L1
L2 = [x ** 2 for x in range(10)]
print L2
L3 = [(x, y) for x in [1, 2, 3] for y in [1,2, 3] if x != y]
print L3
vec = [0, -1, 2, 3, 90, 101, 56]
vec.sort()
print vec
print [abs(x) for x in vec]
freshfruit = [" apple", " oragnge   "]
new_freshfruit = [fruit.strip() for fruit in freshfruit]
print new_freshfruit
vec1 = [[1, 2], [3,4]]
print [num for elem in vec1 for num in elem]
print [str(round(pi, i)) for i in range(1, 6)]
matrix = [[1, 2], [3, 4], [5, 6]]
print [[row[i] for row in matrix] for i in range(2)]
transposed = []
for i in range(2):
    T = []
    for row in matrix:
        T.append(row[i])
    transposed.append(T)
print transposed
A = [1, 2, 3, 4]
del A[1:2]
del A[3:]
print A
