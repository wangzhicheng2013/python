import sys
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
