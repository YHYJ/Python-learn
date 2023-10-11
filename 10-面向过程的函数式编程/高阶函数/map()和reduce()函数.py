#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from functools import reduce

"""Python内建了map()和reduce()函数"""

"""map()函数

map()函数接收两个参数 ——
    一个函数
    一个可迭代对象
map将传入的函数参数依次作用到序列参数的每个元素，并把结果作为新的迭代器返回

举例说明，有一个函数f(x)=x**2
要把这个函数作用在一个list [1, 2, 3, 4, 5, 6, 7, 8, 9] 上
就可以用map()实现如下：
            f(x)=x**2
[ 1  2  3  4   5   6   7   8   9 ]
  |  |  |  |   |   |   |   |   |
[ 1  4  9  16  25  36  49  64  81]
map函数是取出可迭代对象的第一个元素根据函数参数进行计算-
-因此其函数参数仅需要一个参数
"""
# Python代码实现：
r = map(lambda x:x ** 2,[1,2,3,4,5,6,7,8,9,])     # map()的第一个参数是f，即函数对象本身
print(list(r))  # 结果r是一个迭代器（惰性序列），因此通过list()函数将整个序列计算出来

"""
map()作为高阶函数，把运算规则抽象了
因此不但可以计算简单的f(x)=x**2，还可以计算任意复杂的函数
"""
# 比如把list所有数字转为字符串：
print(list(map(str,[1,2,3,4,5,6,7,8,9,])))



"""reduce()函数

reduce函数接收两个参数 ——
    一个函数
    一个序列
reduce把函数参数作用在序列参数上，
并把结果继续和序列的下一个元素做数学形式的累加计算
最终返回的结果根据函数参数的效果决定
reduce函数提取序列参数的前两个元素根据函数参数进行计算-
-并将结果作为下一组的第一个元素再次根据函数参数进行计算-
-因此reduce函数的函数参数的参数应该是两个
"""
# 其效果就是：

# 1、对序列求和
print(reduce(lambda x,y:x + y,[1,3,5,7,9,]))

# 2、将序列[1,3,5,7,9,]转换成整数13579
print(type(reduce(lambda x, y:x*10 + y,[1,3,5,7,9,])),"：",
      reduce(lambda x, y:x*10 + y,[1,3,5,7,9,])
      )

"""
以上两个例子本身没多大用处
但如果考虑到字符串str也是一个序列，
对上面的例子稍加改动，配合map()就可以写出把str转换为int的函数
"""
# reduce()配合map()把str转换为int —— 功能与int()函数相同：
def char2num(s):
    return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5,
                '6': 6, '7': 7, '8': 8, '9': 9}[s]

def str2int(s):
    return reduce(lambda x,y:x*10 + y,map(char2num,s))

print(type(str2int('246810')),"：",
      str2int('246810')
      )



print("*"*25 + "work" + "*"*25)

# map()：
"""利用map()函数，把用户输入的不规范的英文名字变为首字母大写，其他小写的规范名字"""
def normalize(name):
    return name[0].upper() + name[1:].lower()   # 字符串也是可迭代对象

L1 = ['adam', 'LISA', 'barT']
L2 = list(map(normalize,L1))
print(L2)


# reduce()：
"""编写一个prod()函数，可以接受一个list并利用reduce()求积"""
def prod(L):
    return reduce(lambda x,y:x*y,L)

print('3 * 5 * 7 * 9 = ',prod([3,5,7,9,]))


# map() & reduce()
"""利用map和reduce编写一个str2float函数，把字符串'123.456'转换成浮点数123.456"""
def str2float(s):
    def char2num(s):
        return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5,
                '6': 6, '7': 7, '8': 8, '9': 9}[s]
    s1= s.split('.')                                            # 1
    r1 = reduce(lambda x, y:x*10 + y,map(char2num,s1[0]))       # 2
    r2 = reduce(lambda x, y:x*10 + y,map(char2num,s1[1]))       # 3
    r3 = pow(10,len(s1[1]))                                     # 4
    r = r1 + (r2/r3)
    return r

print('str2float(\'123.456\') =', str2float('123.456'))
"""
1处 —— 将‘123.456’以‘.’为标志分割成['123','456']
2处 —— 将s1下标为0的元素'123'转换为整数123
3处 —— 将s1下标为1的元素'456'转换为整数456
4处 —— pow(x,y) 方法返回 x的y次方 的值，此为1000
map()函数先将‘123.456’reduce()"""