#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""set和dict类似，也是 一组key（键）的集合但不存储value（值）.
由于key不能重复，所以，在set中，没有重复的key.
"""


"""一个 Set 是一个不包含重复元素的无序集合.

基本应用是成员资格测试和消除重复元素
"""

#S = {} 或者 set() 都可以创建集合，但想要创建一个空集合必须用 set()，D = {} 创建的是空字典
S = set()
print(S)    #空集合
D = {}
print(D)    #空字典

print('*'*100)


#要以 D = set(...) 格式创建一个set，需要一个list作为输入集合：
s = set([3, 2, 1])    #传入的参数[1, 2, 3]是一个list
print(s)    #显示的 {1, 2, 3} 只是代表这个set内部有1，2，3这3个元素，不表示set是有序的

print('*'*100)


#以 D = {...} 创建一个set则不需要list作为输入集合
basket = {'apple','orange','apple','pear','orange','banana'}
print(basket)   #重复元素在set中自动过滤
print('apple' in basket)    #快速成员检测,有某元素返回True
print('crabgrass' in basket)    #快速成员检测，没有某元素返回False

print('*'*100)


#通过 set 操作从两个词中获得唯一的字母（借助重复元素在set中自动过滤的特性）
a = set('abracadabra')
b = set('alazacam')
print(a)    #在 a 中
print(b)    #在 b 中
print(a - b)    #在 a 中但 不在 b 中
print(a | b)    #在 a 或 b 中
print(a & b)    #在 a 且在 b 中
print(a ^ b)    #在 a 或 b 中 但 不同时在 两者中

print('*'*100)


#像列表一样，set也有语法
a = {x for x in 'abcdefg' if x not in 'abc'}
print(a)

print('*'*100)


#通过 add(key) 方法添加元素到set，可重复添加但无效：
basket.add(1516)
basket.add(2)
print(basket)

print('*'*100)


#通过 remove(key) 方法删除元素：
basket.remove(1516)   #跟的是key的名字
print(basket)
basket.add(1516)
basket.add(591)

print('*'*100)


"""
set和dict的唯一区别仅在于没有存储对应的value，
但是，set的原理和dict一样，所以，同样不可以放入可变对象，
因为无法判断两个可变对象是否相等，也就无法保证set内部“不会有重复元素”
"""