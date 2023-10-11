#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""遍历打印
其中'bmw'全大写，其它首字母大写
"""


cars = ['audi', 'bmw', 'subaru', 'toyota']
for car in cars:
    if car == 'bmw':
        print(car.upper())
    else:
        print(car.title())


'''查询顾客要求的配料是否有存货.

'''
have_foods = ['鸡肉', '虾仁', '辣椒', '香菇', '葱末', '大蒜', '芝麻']
requ_foods = ['臭豆腐', '萝卜', '白菜', '辣椒', '香菇']
for requ_food in requ_foods:
    if requ_food in have_foods:
        print('加上'+requ_food+'。')
    else:
        print('没有'+requ_food)


'''用户创建.

检查新创建的用户名是否重复并给予提示.
不论大小写.
'''
old_users = ['13', '1516', 'YJ', 'YHYJ', 'YJ1516', '妖君']
new_users = input('请创建你的用户名：')

while str(new_users).lower() in str(old_users).lower():
    print('用户 ' + new_users + ' 已存在，请重试')
    new_users = input('请创建你的用户名：')
else:
    print('用户 ' + new_users + ' 创建成功')
