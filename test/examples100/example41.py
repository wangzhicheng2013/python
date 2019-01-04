import sys
def func():
    var = 0
    var += 1
    print 'var = %d' %var
for i in range(3):
    func()
class Static:
    var = 5
    def func(self):
        self.var += 1
        print 'var = %d' %self.var
s = Static()
for i in range(3):
    s.func()

