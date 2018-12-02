import sys
orgin_high = 100
total_high = 0
for i in range(10):
    every_high = orgin_high / 2.0
    total_high += orgin_high + every_high
    orgin_high = every_high
    if 9 == i:
        print every_high
print total_high
    
    
