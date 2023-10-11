#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
del语句 ——根据下标删除元素
pop() ——根据下标删除元素
判断使用 del 还是pop()
remove() ——根据值删除元素
"""


# clear()——清空列表元素但不删除列表
print('*'*25, 'clear()', '*'*25)
motorcycles = ['honda', 'yamaha', 'suzuki']
motorcycles.clear()
print(motorcycles)


# del语句 ——根据下标删除元素
print('*'*25, 'del语句', '*'*25)
'''知道要删除元素的下标可以使用del'''
motorcycles1 = ['honda', 'yamaha', 'suzuki']
del motorcycles1[1]
print(motorcycles1)
# del  motorcycles1     # 直接删除这个列表
'''del可删除任何知道下标的元素，使用del删除的元素无法再访问'''


# pop() ——根据下标删除元素
print('*'*25, 'pop()', '*'*25)
'''pop()可根据下标删除列表的元素，并能够接着使用这个元素，对pop(弹出)来说
列表就像一个栈，而删除元素相当于弹出栈的元素
'''
motorcycles2 = ['honda', 'yamaha', 'suzuki']
popped_motorcycles2 = motorcycles2.pop(1)  # 弹出第1个元素并存储到变量popped_motorcycles2
print(motorcycles2)  # 使用pop弹出元素，元素已不在列表中
print(popped_motorcycles2)  # 仍可通过popped_motorcycles2访问弹出的值


# 判断使用 del 还是pop()
'''
如果从列表删除一个元素，并且不再使用它，就使用del
要在删除元素后还能继续使用该元素，就使用方法　pop()
'''


# remove() ——根据值删除元素
print('*'*25, 'remove()', '*'*25)
'''不知道要删除的元素的下标，只知道要删除的元素的值，可使用remove()
remove()方法删除的元素可以接着使用它的值
'''
motorcycles3 = ['honda', 'yamaha', 'suzuki']
too_expensive = 'yamaha'    # 将删除的元素保存在一个变量
motorcycles3.remove(too_expensive)
print(motorcycles3)
print("\nA " + too_expensive.title() + " is too expensive for me.") #接着使用眼熟的元素
'''如果列表中有重复元素，remove()只删除列表中指定的元素的所有重复中的第一个'''
