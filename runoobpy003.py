# coding:utf-8
__author__ = '王丰宁'
'''
一个整数，它加上100和加上268后都是一个完全平方数，请问该数是多少？
'''
from math import *

r = int((268-100)/2)
for i in range(r*r+1):
    x = int(sqrt(i + 100))
    y = int(sqrt(i + 268))
    if (x * x == i + 100) and (y * y == i + 268):
       print i


