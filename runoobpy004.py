# coding:utf-8
__author__ = '王丰宁'
'''
输入某年某月某日，判断这一天是这一年的第几天？
'''

year = int(raw_input('year:\n'))
month = int(raw_input('month:\n'))
day = int(raw_input('day:\n'))

ms = (0,31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30)
s = sum(ms[0:month]) + day
if ((year % 400 == 0) or ((year % 4 == 0) and (year % 100 != 0))) and (month > 2):
    s += 1
print 'it is the %dth day.' % s