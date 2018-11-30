import sys
Tn = 0
Sn = []
n = int(raw_input("n = "))
a = int(raw_input("a = "))
for i in range(n):
    Tn += a
    a = a * 10
    Sn.append(Tn)
Sn = reduce(lambda x, y: x + y, Sn)
print Sn
            
