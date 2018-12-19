import sys
def Fun(num):
    if num <= 0 or num > 1000000:
        raise TypeError("input invalid...!")
    s = 0
    tmp = num
    while (num):
        s = s * 10 + num % 10
        num /= 10
    return tmp == s
print Fun(121)
print Fun(1122)
num_str = raw_input("number = ")
Len = len(num_str)
flag = True
for i in range(Len / 2):
    if (num_str[i] != num_str[-1 - i]):
        flag = False
if False == flag:
        print "No"
else:
     print "Yes"

