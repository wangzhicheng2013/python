import sys
print ("\tAA\tBB\tCC".expandtabs(8))
str = "helloXXworldhello"
print (str.find("hello"))
print ("1 + 1 = {0}".format(1 + 1))
print ("{0} {1} {1} {0}".format("hello", "world"))
site = {"address" : "123", "name" : "456"}
print ("A : {address}, B : {name}".format(**site))
mylist = ["AA", "BB"]
print ("A : {0[0]}, {0[1]}".format(mylist))
class Default(dict):
    def __missing__(self, key):
        return key
print ("{name} in {country}".format_map(Default(name="AA")))
