import sys
L = []
for i in range(3):
    L.append([])
    for j in range(3):
        number = int(raw_input("number = "))
        L[i].append(number)
print L
total = 0
for i in range(3):
    total += L[i][i]
print total
