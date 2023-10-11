#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""--------------- 统计分数 ----------------"""

'''scores.txt
刘备 ：23  35  44  47  51
关羽 ：60  77  68
张飞 ：97  99  89  91
诸葛亮：100
'''

with open('./Data/scores.txt') as fi:
    filines = fi.readlines()    # 用readlines把每一行分开，便于之后的数据处理

# 对每一条数据进行处理，按照空格，把姓名、每次的成绩分割开
results = []
for line in filines:
    data = line.split()
    one = 0         # 分别计算每个学生的总成绩并记录
    for score in data[1:]:  # data[1:]是每个学生的所有成绩组成的list
        one += int(score)   # one是每个学生的总成绩，所以每次循环都要先对one清零
    result = '%s\t:%d\n'%(data[0],one)  # 对于每一行分割的数据，data[0]是姓名
    results.append(result)
print(results)

with open('./Data/onescores.txt','w') as output:
    output.writelines(results)