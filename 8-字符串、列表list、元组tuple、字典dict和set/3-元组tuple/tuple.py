#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
元组——tuple，另一种有序列表
类似list，但是tuple一旦初始化就不能修改
没有append()，insert()，pop()这样的方法
因为tuple不可变，所以代码更安全
如果可能，能用tuple代替list就尽量用tuple
形式也不一样——
    list：  s = [……，……，……]
    tuple： s = (……,……,……)
"""

# 元组示例
print('*'*25, '元组示例', '*'*25)
print(('Mike', 23))
print('%s is %d years old' % ('Mike', 23))
'''('Mike', 23)就是一个元组，这是元组最常见的用处'''


# 创建元组可以不加括号,元组有和list同样的索引、切片、遍历等操作
print('*'*25, '元组的索引、切片、遍历', '*'*25)
t = (123, 456, 'he')
# 索引
print(t[0])
# 遍历
for i in t:
    print(i)
# 切片
T = t[:2]
print(T)


# 拆封元组
print('*'*25, '拆封元组', '*'*25)
'''序列拆封要求左侧的变量数目与序列的元素个数相同
可变参数只是元组封装和序列拆封的一个结合'''
t_1 = (123, 456, 'he')
x, y, z = t_1
print(x, y, z, t_1)


# 元组的嵌套
print('*'*25, '元组的嵌套', '*'*25)
u = (t, (1, 2, 3))     # 元组u的 2个元素 是另两个元组 t 和 (1,2,3)
print(u)
n = (t, 1, 2, 3)   # 元组n的 4个元素 是另一个元组 t 和 1，2，3
print(n)


# tuple的陷阱
print('*'*25, '元组的陷阱', '*'*25)
'''在定义一个tuple的时候，tuple的元素就必须被确定下来'''
t = (1, 2)
print(t)
# 定义只有一个元素的tuple
t2 = (1)
print(type(t2), t2)
'''定义的不是tuple，是1这个数！
因为括号()既可以表示tuple，又可以表示数学公式中的小括号，这就产生了歧义
因此Py规定，这种情况下，按小括号进行计算，输出结果自然是1，而不是(1)
'''
# 此时，必须加一个逗号来消除歧义
t3 = (1,)
print(t3)


# 定义一个空的tuple
print('*'*25, '定义一个空的tuple', '*'*25)
t1 = ()
print('t1=', t1)


# '可变'的tuple
print('*'*25, "'可变'的tuple'", '*'*25)
tl = ('a', 'b', ['A', 'B'])
print(tl)
tl[2][0] = 'X'
tl[2][1] = 'Y'
print(tl)
'''tuple不可变的意思是
tuple一旦指向一个对象，就不能改成指向另一个
但是tuple所指向的对象本身可变
'''


# 元组作为返回值
print('*'*25, "元组作为返回值", '*'*25)
def get_pos(n):
    """
    :param n: 
    :return: 
    """
    return n/2, n*3
'''得到该返回值的两种方法：'''''
# 1：根据返回值元组中的元素的个数提供变量
x, y = get_pos(10)
print('x=', x, 'y=', y)
# 2：用一个变量记录返回的元组
pos = get_pos(10)
print('pos[0]=', pos[0], 'pos[1]= ', pos[1])


# work
print('*'*25, "work", '*'*25)
foods = ('鱼', '虾', '蟹', '肉', '菜')
# 循环打印食品
for food in foods:
    print(food)
# 尝试修改一个元素
# foods[0] = '没有鱼'
# print(foods)    # 报错，无法修改
# 改变其中两个元素并循环打印
new_foods = ('没有鱼', '没有虾', '蟹', '肉', '菜')
for new_food in new_foods:
    print(new_food)
