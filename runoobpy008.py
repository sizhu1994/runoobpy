# coding:utf-8
__author__ = '王丰宁'
'''
输出9*9乘法口诀表
'''

for i in range(1,10):
    for j in range(1,i+1):
        print '%d * %d = % -3d\t' %(j, i, j*i),
    print '\n'
