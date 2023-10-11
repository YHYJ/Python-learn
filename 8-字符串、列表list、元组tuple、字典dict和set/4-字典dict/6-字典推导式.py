#!/usr/bin/env python3
# -*- coding: utf-8 -*-

""""""

# 列表推导式
print({x: (x+1)**2 for x in (2, 4, 6, 8)})


# 列表推导式的应用
'''合并两个列表成字典'''
list_1 = ['name', 'age', 'gender', ]
list_2 = ['1516', '19', 'man', ]
dic_1 = {list_1[i]: list_2[i] for i in range(len(list_1))}
print(dic_1)

'''zip()
把两个列表转为[(), (), ()]'''
dict_2 = dict(zip(list_1, list_2))
print(dict_2)

'''键值对互转'''
dict_3 = dict_2.copy()
dict_4 = {}
for k, v in dict_3.items():
    dict_4[v] = k
print(dict_4)
