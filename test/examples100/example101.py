import sys
import re
from re import fullmatch
re_str = r"a.b"
result = fullmatch(re_str, "a|b")
print (result)

re_str = r"\w..."
result = fullmatch(re_str, "_XXX")
print (result)

re_str = r"\s..."
result = fullmatch(re_str, " XXX")
print (result)

re_str = r"\d\d\d"
result = fullmatch(re_str, "213")
print (result)

re_str = r"abc\b\saaa"
result = fullmatch(re_str, "abc aaa")
print (result)

re_str = r"^\d\d\d"
result = fullmatch(re_str, "123")
print (result)

re_str = r"abc$"
result = fullmatch(re_str, "abc")
print (result)

re_str = r"\W..."
result = fullmatch(re_str, "@XXX")
print (result)

re_str = r"and\BYou"
result = fullmatch(re_str, "andYou")
print (result)

re_str = r"[abc]CCC"
result = fullmatch(re_str, "cCCC")
print (result)

re_str = r"[91-]"
result = fullmatch(re_str, "-")
print (result)

re_str = r"[^abc]..."
result = fullmatch(re_str, "Dddd")
print (result)

re_str = r"[+-]?[1-9]\d*"
result = fullmatch(re_str, "+123")
print (result)

re_str = r"[\da-zA-Z]{6,16}"
result = fullmatch(re_str, "1A123456")
print (result)

re_str = r"[a-z]{3}|[0-9]{4}"
result = fullmatch(re_str, "abc")
print (result)

re_str = r"\d[a-zA-Z]{3}"
result = fullmatch(re_str, "3abc")
print (result)

re_str = r"([a-z]{3})-(\d{2})\2"
result = fullmatch(re_str, "aaa-2323")
print (result)

re_str = r"\d{2}\.\d{2}"
result = fullmatch(re_str, "22.22")
print (result)

re_str = r"(\d{3})\1([a-z]{2})\2\1"
result = fullmatch(re_str, "123123bbbb123")
print (result)

re_obj = re.compile(r'\d+')
print (re_obj)
print (re_obj.fullmatch('12345'))
print ('------------')
re_str = r'\d+'
str1 = 'abc34jshd8923jkshd9lkkk890k'
result = re.search(re_str, str1)
while result:
    print(result)
    str1 = str1[result.end():]
    result = re.search(re_str, str1)

re_str = r'(\d+)k([a-d]+)'
str1 = 'abc34kshd8923kabcshd9lkkk890kaa'
result = re.findall(re_str, str1)
print(result)
