#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""正常情况下，当定义了一个类并创建了它的实例后
可以给该实例绑定任何属性和方法"""


class Student(object):
    pass

s = Student()
s2 = Student()
s.name = 'Michael'      # 动态的給实例绑定一个属性
print(s.name)

def set_age(self,age):  # 定义一个函数作为实例方法
    self.age = age

from types import MethodType
s.set_age = MethodType(set_age,s)   # 给实例绑定一个方法
s.set_age(25)       # 调用实例方法
print(s.age)        # 输出age的值，测试结果
'''给一个实例绑定的方法，对另一个实例是不起作用的'''

'''为了给所有实例都绑定方法，可以给class绑定方法'''
def set_score(self,score):
    self.score = score

Student.set_score = set_score

# 给class绑定方法后，所有实例均可调用：
s.set_score(100)
print(s.score)
s2.set_score(96)
print(s2.score)

'''通常情况下，上面的set_score方法可以直接定义在class中
但动态绑定允许在程序运行的过程中动态给class加上功能，这在静态语言中很难实现
'''


"""想要限制实例的属性，比如只允许对Students实例添加name和age属性

Py允许在定义class的时候定义一个特殊的__slots__变量来限制该class实例能添加的属性
__slots__定义的属性仅对当前类实例起作用，对继承的子类是不起作用的-
-除非在子类中也定义__slots__，这样，子类实例允许定义的属性就是自身的加上父类的__slots__
"""
class Students():
    __slots__ = ('name','age')      # 用tuple定义允许实例绑定的属性名称

st = Students()
st.name = 'Mark'    # 绑定属性name
st.age = 23         # 绑定属性age
# st.score = 99.5     # 绑定属性score失败