import sys
array = []
N = 100
for i in range(N):
    array.append(i + 1)
print array
for i in range(N / 2):
    array[i], array[N - i - 1] = array[N - i - 1], array[i]
print array
