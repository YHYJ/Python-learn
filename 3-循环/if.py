#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""if
每条if语句的核心都是一个值为True或False的表达式，这种表达式被称为条件测试.
Python根据条件测试的值为True还是False来决定是否执行if语句中的代码:
如果条件测试的值为True，Python就执行紧跟在if语句后面的代码;
如果为False， Python就忽略这些代码
"""


car = 'audi'
print(car == 'AUdi')  # 输出False,因为Python区分大小写
print(car.upper() == 'AUDI')    # 如果大小写不重要可以先统一化

print('*'*50)

'''确定列表非空.

'''
foods = ['鸡', '鸭', '鱼']
if foods:   # 如果列表为空，返回False并执行else后语句
    print('我还有食材')
else:
    print('什么都没了')

print('*'*50)


# ======== 输入一个x的值，一个y的值，判断(x,y)所在象限 ======== #
value = 1
while value:
    x = float(input('请输入x的值：'))
    y = float(input('请输入y的值：'))
    if x == 0:
        if y == 0:
            print('(%.1f,%.1f)在原点' % (x, y))
        elif y > 0:
            print('(%.1f,%.1f)在y轴正半轴' % (x, y))
        else:
            print('(%.1f,%.1f)在y轴负半轴' % (x, y))
    if x > 0:
        if y == 0:
            print('(%.1f,%.1f)在x轴正半轴' % (x, y))
        elif y > 0:
            print('(%.1f,%.1f)在第一象限' % (x, y))
        else:
            print('(%.1f,%.1f)在第四项限' % (x, y))
    if x < 0:
        if y == 0:
            print('(%.1f,%.1f)在x轴负半轴' % (x, y))
        elif y > 0:
            print('(%.1f,%.1f)在第二象限' % (x, y))
        else:
            print('(%.1f,%.1f)在第三项限' % (x, y))
    value = 0
