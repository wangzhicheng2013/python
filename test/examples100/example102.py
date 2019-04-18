str = "abcd"
print (str.capitalize())
str = "a,bcd ED"
print (str.capitalize())
print ("KKKL".casefold())
str = "ABCddd"
sub = "Cd"
print (str.count(sub, 0, 100))
str = "我们"
str = str.encode("UTF-8")
print (str)
str = "我们"
str = str.encode("GBK")
print (str)
str = str.decode("GBK")
print (str)
str = "123456ABCabc"
print (str.endswith("abc", 6))
