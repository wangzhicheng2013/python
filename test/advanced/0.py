import sys
class Stu:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def __str__(self):
        return self.name
    def __format__(self, key):
        fmt = self.mydict[key]
        print (fmt)
        return fmt.format(obj=self)
    def __del__(self):
        print ("obj destruct.")
    mydict = {
        'n-a' : '{obj.name}-{obj.age}'
    }

s0 = Stu("zhangsan", 18)
print (s0)
format (s0, 'n-a')
class A:
    def __init__(self, num):
        self.num = num
a = A(10)
print (a.__dict__)
class Foo:
    def __init__(self, name):
        self.name = name
    def __getitem__(self, item):
        return self.__dict__[item]
    def __setitem__(self, key, value):
        self.__dict__[key] = value
    def __delitem__(self, key):
        self.__dict__.pop(key)
foo = Foo(100)
print (foo.__dict__)
foo["aa"] = 1000
print (foo["aa"])
L = ['1', 2, 'a']
print (L)
L.pop(0)
print (L)
print (L[1].upper())
print("\033[5;31;40mLinux\033[0m")
