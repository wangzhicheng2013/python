import sys
import math
print dir(sys)
x = 2 * 0.01
y = 20 - 56 * 7 / 0.123
print "hello world" + repr(x + y)
print (repr(x - y), "11", "22A")
for i in range(1, 11):
    print (repr(i).rjust(2), repr(i * i).rjust(4))
for i in range(1, 11):
    print('{0} {1} {2})'.format(i, i * i, i * i * i))
print "12".zfill(10)
print "-8.99012".zfill(10)
print "A = {}".format('C')
print ("{1} and {0}".format('C', 'A'))
print "This is {food}".format(food = "C")
print "This is {0}".format(math.pi)
print "This is {0:3f}".format(math.pi)
table = {"K0":123, "K1":1234, "K2":12345}
for k, v in table.items():
    print "{0:10} ==> {1:10d}".format(k, v)
table = {"K0":123, "K1":1234, "K2":12345, "K3":123456}
print "K0:{0[K0]:d};K1:{0[K1]:d};K3:{0[K2]:d};K3:{0[K3]:d}".format(table)
print "PI is {0:3.5f}".format(math.pi)
file1 = open("./add.py", "r+")
L = list(file1)
print L
for line in file1:
    print line
value = ("the A is", 18)
s = str(value)
file1.write(s)
file1.close()
with open("./add.py") as f:
    r = f.read()
    print r
f.closed
