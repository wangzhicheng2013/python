import sys
def do_local():
    spam = "123"
def do_global():
    global spam
    spam = "12345"
spam = "test"
print spam
do_local()
print spam
do_global()
print spam
class MyClass:
    i = 180
    def __init__(self):
        self.i = 120
    def show(self):
        print "My Class"
        print self.i
myClass = MyClass()
myClass.show()
fun = myClass.show
fun()
class Cat:
    kind = "Tom"
    def __init__(self, kind):
        self.kind = kind
    def Show(self):
        print self.kind
def TT(self):
    print "TT"
class Cat1:
    f = TT
    def __init__(self):
        self.data = []
    def Append(self, name):
        self.data.append(name)
cat = Cat("Jenny")
cat.Show()
cat1 = Cat1()
cat1.f()
cat1.Append("ABC")
print cat1.data
