# coding:utf-8
__author__ = '王丰宁'
'''
判断101-200之间有多少个素数，并输出所有素数
'''
from math import sqrt

def jdprime(n):
    r = int(sqrt(n))+1
    leap = 1
    for i in range(2,r):
        if n%i ==0:
            leap = 0
            break
    return leap
cout = 0
for i in range(101,201):
    if jdprime(i) == 1:
        cout +=1
        print i
print '101-200之间共有%d个素数' %cout