# coding:utf-8
__author__ = '王丰宁'
'''
斐波那契数列
'''

def fib(n):
    if n == 1:
        return [1]
    fibs = [1,1]
    for i in range(2,n):
        fibs.append(fibs[-1] + fibs[-2])
    return fibs
