#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""模块itertools提供了非常有用的用于操作迭代对象的函数"""


import itertools


# ---------------itertools提供的几个“无限”迭代器--------------- #
# count()——创建一个无限的迭代器
natuals = itertools.count(1)    # count()创建一个无限的迭代器
# for n in natuals:
#     print(n)
'''上述代码会打印自然数序列而不停止'''
# cacly()——把传入的一个序列无限重复下去
cs = itertools.cycle('abc')     # cycle()把传入的一个序列无限重复下去
value = 0
for c in cs:
    print(c)
    value += 1
    if value >= 15:
        break
'''上述代码不加限制，会挨次打印a、b、c不停止'''
# repeat()——把一个元素无限重复，但第二个参数可以限制重复次数
re = itertools.repeat('AB', 5)
for r in re:
    print(r)


"""无限序列只有在用for迭代时才会无限地迭代下去
如果只是创建了一个迭代对象，它不会事先把无限个元素生成出来-
-事实上也不可能在内存中创建无限多个元素"""


# takewhile()——截取有限数列
'''无限序列虽然可以无限迭代，但通常用takewhile()等函数根据条件判断来截取出一个有限的序列'''
natuals_1 = itertools.count(2)
ns_1 = itertools.takewhile(lambda x: x <= 10, natuals_1)
print(list(ns_1))


# ---------------itertools提供的几个迭代器操作函数--------------- #
# chain()——把一组迭代对象串联起来，形成一个更大的迭代器
x = []
for c in itertools.chain('ABC', '123', 'XYZ', ['9', '8', '7']):
    print(c)
    x.append(c)
print(x)
# groupby()——把迭代器中【相邻】的重复元素挑出来放在一起
'''挑选规则是通过函数完成的
只要作用于函数的两个元素返回的值相等，这两个元素就被认为是在一组的
将函数返回值作为组的key'''
for key, group in itertools.groupby('AABBBbbBCCANB114125424'):
    print(key, list(group))
'''要忽略大小写进行分组，可以让元素'A'和'a'都返回相同的key：'''
for key_1, group_1 in itertools.groupby('AaaBbBcCCAaBb', lambda c: c.upper()):
    print(key_1, list(group_1))


"""小结：
itertools模块提供的全部是处理迭代功能的函数
它们的返回值不是list，而是Iterator，只有用for循环迭代的时候才真正计算
"""