#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""字典(dict)是Py中的基本类型，在其他语言中也称为map
字典这种[数据结构]类似通讯录，有一个名字和这个名字对应的信息
在字典中：名字叫做【键】，对应的信息叫做【值】
字典就是一个键/值对的集合
"""


# 字典的基本格式
'''字典的基本格式是：
d = {key1 : value1 ，key2 : value2}
   ——key是‘键’，value是‘值’
键/值对用冒号分割，每个队之间用逗号分割，整个字典包括在花括号中
'''''
# 关于字典
'''关于字典：
1、键必须是唯一的
2、键只能是 不可变 对象，比如字符串、整数、浮点数、bool值。
   像list就不能作为键，但可以作为值
3、值可以是Python中的任意一种对象
4、字典是一种动态结构，可随时在其中添加键—值对
'''


# 简单的字典栗子
print('*' * 25 + '简单的字典栗子' + '*' * 25)
score = {
    '萧峰': 95,
    '段誉': 97,
    '虚竹': 89,
    '1516': 100,
    }
print(score)


# 获得包含字典中所有 键 的列表和 值 的列表
print('*' * 25 + '获得包含字典中所有 键 的列表和 值 的列表' + '*' * 25)
print('score中的键有：', list(score.keys()))   # 键的列表
print('score中的值有：', list(score.values()))  # 值的列表
print(list(score.items()))
print(list(score))    # 只获得键
print(score.keys())    # 获得字典的键
print(score.values())    # 获得字典的值
print(sorted(score.keys()))     # 通过sorted对键进行排序，键的类型要相同
print(sorted(score.values()))   # 通过sorted对值进行排序，值的类型要相同


# Py字典中的键值对没有顺序，无法用索引访问字典中的某一项，而是要用键来访问
print('*' * 25 + '访问dict' + '*' * 25)
print(score['段誉'])
print(score['1516'])
'''如果键是字符串，通过键访问的时候就需要加引号，如果是数字作为键则不用'''


# 如果要改变某一项的值，就直接给这一项赋新值：
print('*' * 25 + '改变字典里键的值' + '*' * 25)
score['1516'] = 150
print(score['1516'])


# 增加一项字典项的方法就是直接定义一个新键并赋值：
print('*' * 25 + '增加一项字典项' + '*' * 25)
score['慕容复'] = 60
for name in score:
    print(name, score[name])


print('*' * 25 + '删除字典项' + '*' * 25)
'''转4-字典的拷贝和删除.py'''


# 新建一个空字典：
print('*' * 25 + '新建空字典' + '*' * 25)
d = {}
d['a'] = 100
d[2] = 200
print(d)


# 从含有键值对的列表中提取字典
print('*' * 25 + '从含有键值对的列表中提取字典' + '*' * 25)
'''用 dict 方法直接从含有 key-value 的序列中定义一个字典'''
print(dict([('a', 1), ('b', 2), ('c', 3)]))
'''当键是简单的字符串时，可以用键为参数直接指定对象'''
print(dict(a=1, c=3, b=2))
'''利用字典推导式从随机的key和value的表达式中创建字典'''
print({x: (x+1)**2 for x in (2, 4, 6, 8)})


# 判断字典中有没有某个键
print('*' * 25 + '判断字典是否含有某个键' + '*' * 25)
# in/not in
print('a' in score)
print('b' not in score)
'''有就返回True,没有返回False'''
# get()
print(score.get('you', '没有'))
print(score)
''''you'是在字典中查找的key
当字典里有这个key时，显示其对应的value，没有时显示第二个参数指定的内容
默认None
'''


"""dict的key必须是不可变对象.
这是因为dict根据key来计算value的存储位置，
如果每次计算相同的key得出的结果不同，那dict内部就完全混乱了
这个通过key计算位置的算法称为 —— 哈希算法（Hash）
"""
with open('test.txt', 'r+') as fi:
    fi.write('www' + ' ')
    fi.write('123' + '\n')
    ff = fi.readlines()
    print(type(ff), ff)
    for file in ff:
        print(type(file), file)