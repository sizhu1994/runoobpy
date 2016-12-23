# coding:utf-8
__author__ = '王丰宁'

i= int(raw_input('净利润：'))
arr = [10,6,4,2,1,0]
arr = [x*100000 for x in arr]
rat = [1, 1.5, 3, 5, 7.5, 10]
rat = [x*0.01 for x in rat]
r = 0
for idx in range(0,6):
    if i>arr[idx]:
        j =(i - arr[idx])*rat[idx]
        r += j
        i = arr[idx]
print r