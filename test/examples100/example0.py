#coding=utf-8
'''
有四个数字：1、2、3、4，能组成多少个互不相同且无重复数字的三位数？各是多少？
'''
import sys
numbers = [1, 2, 3, 4]
for i in numbers:
    for j in numbers:
        for k in numbers:
            if (i != j) and (i != k) and (j != k):
                print i, j, k

