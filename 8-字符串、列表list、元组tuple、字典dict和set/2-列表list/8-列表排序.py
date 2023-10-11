#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""排序时列表里的元素类型只能是一种类型
sort() ——对列表进行永久排序
sorted()　——对列表进行临时排序
reverse() ——逆置列表
reversed()——临时逆置列表
"""


# sort() ——对列表进行永久排序
print('*'*25, 'sort()', '*'*25)
cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort()     # 按照字母顺序正序排列元素，再无法恢复到原顺序
print(cars)
cars.sort(reverse=True)     # 反序排列，只需加 reverse = True
print(cars)


# sorted()　——对列表进行临时排序
print('*'*25, 'sorted()', '*'*25)
'''不将逆置结果重新赋给cars1的话，原列表cars1里的元素顺序不变'''
cars1 = ['bmw', 'audi', 'toyota', 'subaru']
print('这是原始顺序：', cars1)
print('这是按照字母顺序：', sorted(cars1))
print('这是按照反向字母顺序：', sorted(cars1, reverse=True))
print('核实原列表顺序不变：', cars1)


# reverse() ——逆置列表
print('*'*25, 'reverse()', '*'*25)
cars2 = ['bmw', 'audi', 'toyota', 'subaru']
cars2.reverse()  # reverse()　永久倒序排列列表，要恢复原样再次调用reverse()
print(cars2)


# reversed()——临时逆置列表
print('*'*25, 'reversed()', '*'*25)
'''不将逆置结果重新赋给L的话，原列表L里的元素顺序不变'''
L = ['dream', 'a', 'have', 'I']
print(list(reversed(L)))
print(L)
print(L.__reversed__())
