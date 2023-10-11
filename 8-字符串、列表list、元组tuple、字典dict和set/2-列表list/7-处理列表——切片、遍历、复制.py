#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
列表切片
遍历切片
复制列表——浅拷贝/深拷贝
"""


say = ['I', 'am', 'fime', 'thank', 'you', 'and', 'you']

# 列表切片
print('*'*25, '列表切片', '*'*25)
'''创建切片，需指定要使用的首个元素和末位元素的索引
类似range到达末位元素时停止'''
print(say[0:3])  # 打印列表 say 的切片包含前三个元素，输出也是一个列表
print(say[1:5])  # 可以是任何子集，例如第２～５个元素
print(say[:3])   # 不指定第一个索引，默认为０
print(say[3:])   # 不指定终止索引，默认为０
print(say[:])    # 都不指定，全部输出
print(say[-4:])  # 切出倒数第四个到最后
print(say[-4:-1])   # 切出倒数第四到倒数第一之间


# 遍历切片
print('*'*25, '列表切片', '*'*25)
'''如果要遍历列表的部分元素，可在for循环中使用切片'''
# 遍历前三名队员并打印名字
players = ['charles', 'martina', 'michael', 'florence', 'eli']
print('队伍前三名队员：')
for player in players[:3]:
    print(player.title())


# 复制列表
print('*'*25, '复制列表', '*'*25)
'''根据既有列表创建全新的列表.
可创建一个包含整个列表的切片-
-方法是同时省略起始索引和终止索引（[:]）'''
my_foods = ['海鲜', '鲤鱼', '冷饮', '火锅']
'''浅拷贝'''
f_foods = my_foods   # 这种方法是把f_foods关联到包含在my_foods中的列表，两个变量指向同一个列表
f_foods.append('豆腐')   # 因此添加到f_foods的元素也会添加到my_foods
my_foods.append('豆腐脑')     # 同理
print(f_foods)
print(my_foods)
'''深拷贝'''
# 应该这样写来避免此问题
f_foods = my_foods[:]
f_foods.append('豆腐')
my_foods.append('豆腐脑')
print(f_foods)
print(my_foods)
# 或者用copy()函数
f_foods = my_foods.copy()     # 返回新列表
