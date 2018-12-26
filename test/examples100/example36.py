import sys
import math
def fun(n):
    j = int(math.sqrt(n))
    for i in range(2, j + 1):
        if 0 == n % i:
            return False
    return True
if __name__ == '__main__':
        for i in range(2, 101):
            if True == fun(i):
                print i
    
    
