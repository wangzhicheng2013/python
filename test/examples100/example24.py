import sys
numerator = 2.0
denominator = 1
s = 0
for i in range(21):
    s += numerator / denominator
    t = numerator + denominator
    denominator = numerator
    numerator = t
