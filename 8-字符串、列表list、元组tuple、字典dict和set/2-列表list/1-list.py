#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""list——“列表”，用来处理一组有序项目的数据结构"""


# 遍历输出列表i的元素
i = [0,1,3,5,7,9,'aaabbbccc',3.14,True,'你好']
for n in i:
    print(n)


# list中的元素可以是另一个list:
s = ['python','java',['VB','php'],True]
print(len(s))       # 长度为4，只有4个元素！！
# 可以拆为：
p = ['VB','php']
s = ['python','java',p,True]
# 要拿到'php'。可以 p[1] 或者 s[2][1] ,因此s可以看成是一个二维数组，类似的还有三维、四维……数组，不过很少用到


# 如果一个list中一个元素也没有，就是空的list，长度为0
