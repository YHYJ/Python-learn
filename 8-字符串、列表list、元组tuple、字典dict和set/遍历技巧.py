#!/usr/bin/env python3
# -*- coding: utf-8 -*-


# 遍历字典（dict）数据时,可以用 items() 方法同时把关键字和相对应的值从字典中取出
dictionary = {'张三': 70, '李四': 80, '王二麻子': 90}
for k, v in dictionary.items():
    print(k, v)
'''同：

for x in dictionary:
    print(x,dictionary[x])
'''

print('*'*100)


# 遍历序列数据时，可以用 enumerate() 同时把位置索引和对应的值得到
for i, v in enumerate({'a', 'b', 'c'}):    # enumerate里的数据可以是 任意类型
    print(i,v)

print('*'*100)


#同时遍历两个及以上序列时，可以用 zip() 把属性整合起来
questions = ['名字','年龄','爱好']
answers = ('YJ',20,'music')     #两个序列类型可以不同
for q,a in zip(questions,answers):
    print('你的{0}是？{1}.'.format(q,a))

print('*'*100)


#倒叙遍历序列，首先要正序指定遍历的数列，然后调用方法 reversed()
for i in reversed(range(1,10,2)):
    print(i)    #先正序排列1,3,5,7,9  再倒序输出
L = (1,2,3,4,5,6)
for n in reversed(L):
    print(n)

print('*'*100)


#想要有序遍历数列但不改变原数列用sorted()
fruit = ['banana','durian','grape','orange','pear','apple']
for f in sorted(fruit):
    print(f)
print(fruit)