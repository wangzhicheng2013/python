import sys
if __name__ == '__main__':
    Persons = {"zhangLi" :19, "LiMing" : 28, "PengYou" : 20, "ZhuRenYi" : 38, "LeiJun" : 17}
    age = 0
    name = ""
    for key in Persons.keys():
        if Persons[key] > age:
            age = Persons[key]
            name = key
    print "name = %s, age = %d" %(name, age)
            
            


