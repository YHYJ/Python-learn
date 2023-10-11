#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import random
random.seed()   #伪随机数生成模块，如果不提供 seed，默认使用系统时间。使用相同的 seed，可以获得完全相同的随机数序列，常用于算法改进测试。
num = random.randint(-10,10)    #生成一个[-10,10]之间的随机整数
print(num)

'''random模块中其他常用方法'''
#1：random.random()————不需要参数，随机生成一个[0.0,1.0)之间的浮点数
num = random.random()
print(num)

#2：random.uniform(a,b)————随机生成a、b之间的浮点数。a、b无需是整数，也不用考虑大小顺序
num = random.uniform(0.6,9)
print(num)
num = random.uniform(6,0.9)
print(num)

#3：random.choice(seq)————随机从序列中选取一个元素。seq需要是一个序列：list、元组、字符串
print(random.choice([0,1,2,8,5,4,'abc','妖君']))    #包含字符串的list
print(random.choice('hello，妖君'))    #字符串
print(random.choice((1,'a','妖君')))  #元组
seq = ['妖君','YJ',1]
print(random.choice(seq))

print('''#------------------------分隔符------------------------#''')

#4：random.randrange(start,stop,step)————生成一个 [start,stop)，间隔为step的随机数，三个参数都要为整数且start<stop
print(random.randrange(1,9,2))   #从[1，3，5，7]中随机选取一个
#start的默认参数是0，step的默认参数是1.如果需要指定step就必须指定start
print(random.randrange(6))  #指定stop=6，默认start=0，step=1，即[0，1，2，3，4，5]
print(random.randrange(2,6))    #指定start=2，stop=6,默认step=1,即[2,3,4,5]
'''
random.randrange(start, stop, step)
其实在效果上等同于
random.choice(range(start, stop, step))
'''

#5：random.sample(population,x)————从population序列中随机获取x个元素生成一个新序列。sample不改变原序列
print(random.sample([0,1,2,8,5,4,'abc','妖君'],3))    #随机选取出来的元素组成的新序列不按照原序列元素的顺序

#6：random.shuffle(seq)————把序列seq中的元素顺序打乱，shuffle直接改变原有序列
x = [0,1,2,8,5,4,'abc','妖君']
random.shuffle(x)   #不能写成：print(random.shuffle(x))，结果是None
print(x)