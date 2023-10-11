#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Py内建函数filter()用于过滤序列

和map()类似，filter()也接收一个函数和一个序列
和map()不同，filter()把传入的函数参数依次作用于序列参数的每个元素-
-然后根据返回值是True还是False决定保留还是丢弃该元素
"""

"""在一个list中，删掉偶数，只保留奇数"""
# 可以这么写：
print(list(filter(lambda n:n % 2 == 1,[1,2,4,5,6,9,10,15,])))

"""把一个序列中的空字符串删掉"""
# 可以这么写：
print(list(filter(lambda s:s and s.strip(),['A', '', 'B', None, 'C', '  '])))

"""用filter()求素数——埃氏筛法
埃氏筛法——算法解析：
首先，列出从2开始的所有自然数，构造一个序列：
2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,...
取序列的第一个数2，它一定是素数，然后用2把序列中2的倍数筛掉：
3,5,7,9,11,13,15,17,19,...
取新序列的第一个数3，它一定是素数，然后用3把序列的3的倍数筛掉：
5,7,11,13,17,19,...
取新序列的第一个数5，然后用5把序列的5的倍数筛掉：
7,11,13,17,19,...
不断筛下去，就可以得到所有的素数
用Py实现该算法："""
# 先构造一个从3开始的奇数序列：
def _odd_iter():
    n = 1
    while True:     # 没有停止条件
        n += 2
        yield n     # 生成器函数，无限序列

# 构造一个筛选函数
def _not_divisible(n):
    return lambda x:x % n > 0

# 构造返回下一个素数的生成器函数
def primes():
    yield 2
    it = _odd_iter()    # 初始序列
    while True:
        n = next(it)    # 返回it序列的第一个数
        yield n
        it = filter(_not_divisible(n),it)   # 构造新序列

for n in primes():
    if n < 100:
        print(n)
    else:
        break
"""流程为：
primes() —— 刚执行时先返回第一个素数2
it = _odd_iter() —— 构造一个产生被验证序列的生成器
n = next(it) —— 返回it序列的第一个数作为验证序列中的数是否为素数的除数
yield n —— 因为it序列第一个数3一定是素数，所以先返回
it = filter(_not_divisible(n),it) —— 根据筛选函数构造新序列
然后一直返回it序列的下一个元素"""



print("*"*25 + "work" + "*"*25)

"""回数是指从左向右读和从右向左读都是一样的数，例如12321，909"""
# 请利用filter()滤掉非回数：
'''def is_palindrome(n):
    n = str(n)                  # 将n转化为字符串以比较头尾是否一样
    value = len(n)//2      # 获得n的位数的半数，若为奇数长度不计中间的数
    l,x = 0,1                   # l做前半段下标，x做后半段下表
    if l <= value-1:            # 左右两段是否已验证完
        if n[l] == n[-x]:       # 如果前半段和后半段对应位置的数相同
            x -= 1              # 再验证下一相应位置的数字
            return True'''

# 更好的算法：
def is_palindrome(n):
    if n >= 11:
        return str(n) == str(n)[::-1]
    else:
        return False

output = filter(is_palindrome, range(1, 1000))
print(list(output))
"""
相当于：
def is_palindrome(n):
    if n >= 11:
        if str(n) == str(n)[::-1]:
            return n
    else:
        return False
"""