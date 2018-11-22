import sys
from math import sqrt
count = 0
for k in range(101, 201):
    is_prime_flag = True
    loop = int(sqrt(k)) + 1
    for m in (2, loop + 1):
        if (0 == k % m):
            is_prime_flag = False
            break
    if (True == is_prime_flag):
        count = count + 1
        print k
print "total prime = ", count
            
