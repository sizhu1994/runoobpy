# coding:utf-8
__author__ = '王丰宁'
'''
将一个正整数分解质因数。例如：输入90,打印出90=2*3*3*5
'''

def prime_factors(n):
    if not isinstance(n, int) or n <=0:
        print '请输入一个正确的数字！'
        exit(0)
    elif n == 1:
        return [1]
    p = []
    while n not in [1]:
        for i in xrange(2,n+1):
            if n % i ==0:
                n /= i
                p.append(i)
                break
    return p

