import sys
X = [[12, 7, 3], 
  [5, 6, 8],
  [8, 90, 1]]
print X
Y = [[-12, -7, -3], 
  [-5, -6, -8],
  [-8, -90, -1]]
print Y
Z = []
for i in range(3):
    L = []
    for j in range(3):
        L.append(X[i][j] + Y[i][j])
    Z.append(L)
print Z

