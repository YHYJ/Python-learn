#!/usr/bin/env python3
# -*- coding: utf-8 -*-


# 使用 repr() 输出指定数字的平方和立方表格
for x in range(1, 11):
    print(repr(x).ljust(2), repr(x*x).ljust(3), repr(x*x*x).ljust(4))
# ljust() 左对齐函数，参数代表长度，对应的是 rjust() 右对齐函数和 center() 中心对齐行数


print('*'*100)

# 方法 zfile() 使用 0 在字符串 左侧 填充到制定宽度，支持正负号
print('12'.zfill(5))
print('-3.14'.zfill(7))  # 算上负号和小数点一共7位
print('3.14159265358'.zfill(5))  # 不会截断
print('abc'.zfill(5))   # 字符串不非要是数字字符串
# 如果输入的字符串太长以致超出对齐函数的参数，对齐函数并不会截断它而是原样返回，防止输出错误的值
x = '123456789'
print(x.ljust(5)[:5])   # 切片并对齐，[:5]代表切片长度为0~5，ljust(5)代表占用长度为5


print('*'*100)

for x in range(1, 11):
    print('{0:3d}{1:4d}{2:5d}'.format(x, x*x, x*x*x))

print('*'*30, 'str.format() 的基本用法', '*'*30)
print('虎是{}不是{}'.format('猫科动物', '犬科动物')) #将format的参数按顺序传递到{}
print('{0}和{1}'.format('熊猫', 'Panda'))   #{}里的参数为数字是传递的数据的位置
print('{1}和{0}'.format('熊猫', 'Panda'))
print('这是{c}这是{o}'.format(c = '中国',o = '外国'))   #{}中的参数是字符串，它们的值在format中通过参数名指定

import math
print('圆周率是 {}'.format(math.pi))
print('圆周率是 {0:.3f}'.format(math.pi))   #将pi小数部分截取3位，位置参数后面跟‘:’和格式化分类符对格式化进行精确控制

table = {'A':4127,'AB':4096,'ABC':7678}
for name,num in table.items():  #items()方法以列表形式返回可遍历的元组
    print('{0:1}==>{1:5d}'.format(name,num))    #在{}的:后给定一个整数会设置这个字符宽度的【最小数值】，设置数字宽度要用相应的 d 或 f
    #比如为3，则字符宽度最小为3，但其他长于3的字符正常显示，短于3的补空格足3

#对于比较长但不可分割的格式化字符，使用名称代替位置参数来引用被格式化的变量,使用 [] 访问所有主键
print('A:{0[A]:d};\nAB:{0[AB]:d};\nABC:{0[ABC]:d};'.format(table))  #这样format可以只传递一个字典本身
print('A:{A:d};AB:{AB:d};ABC:{ABC:d}'.format(**table))  #简写
