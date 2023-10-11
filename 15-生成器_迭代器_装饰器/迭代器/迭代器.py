#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''迭代器（Iterator）的定义.

可以被next()函数调用并不断返回下一个值的对象.
'''
#可以使用 isinstance() 判断一个对象是否是 迭代器(Iterator)对象：
from collections import Iterator

print(isinstance([1,2,3],Iterator))
print(isinstance({'a': 1,},Iterator))
print(isinstance({1,2,3},Iterator))
print(isinstance((1,2,3),Iterator))
print(isinstance('abc',Iterator))
print(isinstance(100,Iterator))
print(isinstance((x for x in range(1,10)),Iterator))    # 生成器是迭代器
'''生成器都是迭代器对象，
list、dict、set、str、tuple等虽然是可迭代对象，却不是迭代器
对可迭代对象调用__iter__方法获得它的迭代器对象
'''
#迭代器对象表示一个数据流，可以被next()函数调用并不断返回下一个数据
# 直到没有数据时抛出StopIteration错误
# 可以把这个数据流看做一个有序序列
# 因为我们不能提前知道序列的长度，只能不断通过next()函数实现按需计算下一个数据
# 所以迭代器的计算是惰性的，只有在需要返回下一个数据时才会计算
# 迭代器甚至可以表示一个无限大的数据流，例如全体自然数。而使用list是永远不可能存储全体自然数的


print("*"*50)

#把list、dict、set、str、tuple等可迭代对象变成迭代器可以使用iter()函数：
print(isinstance(iter([]),Iterator))


print("*"*50)

#小结：
# 1、凡是可作用于for循环的都是可迭代对象
# 2、凡是可作用于__next()__函数的对象都是迭代器类型，它们表示一个惰性计算的序列
# 3、集合数据类型如　list、dict、str　等是可迭代对象但不是迭代器
#    但可以通过iter()函数获得一个迭代器对象
# 4、Python的for循环本质上是通过不断调用__next()__函数实现的
for i in [2,4,6,8,]:
    pass
## 实际上等价于：
it = iter([1,2,3,])     #通过iter()方法获得list或其他数据类型的迭代器对象
print(it)
print(next(it))
print(next(it))
print(next(it))         #通过next()方法来访问list中的元素
#容器中没有可访问的元素后next()方法抛出一个StopIteration异常终止迭代器


print("*"*50)

#for自动通过iter()方法来获得迭代器对象，并使用next()方法获取下一个元素
for n in range(1,10,2):
    print(n)
