import sys
class Student:
    name = ""
    age = 0
def fun(stu):
    stu.name = "ZhangSan"
    stu.age = 20
if __name__ == '__main__':
    stu = Student()
    fun(stu)
    print stu.name
    print stu.age



            


