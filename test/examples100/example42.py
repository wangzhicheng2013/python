import sys
num = 2
def func():
    num = 1
    print 'internal num = %d' %num
    num += 1
for i in range(3):
    num += 1
    print 'external num = %d' %num
    func()

