import sys
f1 = 1
f2 = 1
for i in range(1, 22):
    print "%12ld %12ld" %(f1, f2)
    if 0 == (i % 8):
        print ''
    f1 = f1 + f2
    f2 = f1 + f2

