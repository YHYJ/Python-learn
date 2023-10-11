#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""面向对象的三大特点 ——
    -数据封装：即类的方法（类的内部定义的访问类的数据的函数），见注释 # 1
    -继承：见four_.py ——
        子类获得父类的所有功能，并可自定义自己独有的功能
        一个实例的数据类型是某个子类，那它的数据类型也是这个子类的父类，见注释 # 2 3
    -多态：子类继承父类所有方法，并可以在自己的代码块中修改任意某个方法（假设为a()）-
        -这样在运行a()时会调用子类修改后的a()方法
"""


class Student(object):

    def __init__(self,name,score):
        """构造函数，在类的实例化时自动调用"""
        self.name = name
        self.score = score

    def priint_score(self):         # 1
        print('%s：%s' % (self.name,self.score))

mark = Student(name='Mark', score=76)
print(mark.name)
mark.name = 'Bell'
print(mark.name)
print(isinstance(mark, Student))     # 2
print(isinstance(mark, object))      # 3
