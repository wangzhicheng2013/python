import sys
def move(array, n, m):
    L = []
    for i in range(m):
        L.append(array[i + n - m])
    L1 = []
    for i in range(n - m):
        L1.append(array[i])
    for i in range(len(L)):
        array[i] = L[i]
    for i in range(len(L1)):
        array[i + len(L)] = L1[i]

array = [2, 8, 6, 1, 78, 45, 34, 2]
n = len(array)
m = 5
move(array, n, m)
print array
