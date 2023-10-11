#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""排序算法

排序是在程序中经常用到的算法
无论使用冒泡排序还是快速排序，排序的核心是比较两个元素的大小
数字可以直接比较，但如果是字符串或者两个dict,直接比较数学上的大小是没有意义的
因此，比较的过程必须通过函数抽象出来
"""

"""sorted()是一个高阶函数：
Python内置的sorted()函数可以对序列进行排序"""
# 如下：
print(sorted([36,5,-2,0,15,19,100,-156,]))    # 排序数字列表，按照数字大小
print(sorted(['36','5','-2','0','-12']))      # 按照有无负号和每个字符串第一个元素的大小
print(sorted((36,5,-2,0,15,19,100,-156,)))    # 排序数字元组，按照数字大小
print(sorted({'l':36,'c':5,'b':-2,'e':0,}))   # 排序字典，按照键


"""sorted()可以接收一个key函数来实现自定义的排序"""
# 例如按绝对值大小排序：
print(sorted([36,5,-2,0,15,19,100,-156,],key=abs))
'''key指定的函数作用于序列的每一个元素，并根据key函数返回的结果进行排序'''



"""sorted()函数对字符串进行排序"""
print(sorted(['dream','a','have','I']))       # 排序字符串列表，按照字符大小写和顺序
'''默认情况下对字符串排序是按照ASCII的大小比较的
由于'I' < 'a'，结果，大写字母I会排在小写字母a的前面'''


"""现在若要求排序忽略大小写，按照字母序排序
只要用一个key函数把字符串映射为忽略大小写排序即可
忽略大小写来比较两个字符串，实际上就是在比较时把字符串都变成大写（或者都变成小写）"""
# 给sorted传入key函数，即可实现忽略大小写的排序：
print(sorted(['dream','a','have','I'],key=str.lower))

# 进行反向排序，不必改动key函数，可以传入第三个参数reverse=True：
print(sorted(['dream','a','have','I'],key=str.lower,reverse=True))

# 小结：用sorted()排序的关键在于实现一个映射函数


print("*"*25 + "work" + "*"*25)

"""假设用一组tuple表示学生名字和成绩："""
L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]
# 请用sorted()对上述列表分别按名字排序：
def by_name(t):
    return t[0]
L1 = sorted(L,key=by_name)
print(L1)

# 按照成绩从高到底排序：
def by_score(t):
    return t[1]
L2 = sorted(L,key=by_score,reverse=True)
print(L2)