#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""对于class的继承关系来说，使用type()就很不方便

要判断class的类型，可以使用isinstance()函数，如果继承关系是：
object -> Animal -> Dog -> Husky
"""

class Animal():
    pass

class Dog(Animal):
    pass

class Husky(Dog):
    pass

a = Animal()
d = Dog()
h = Husky()

print(isinstance(h,Dog))
print(isinstance(h,Animal))
'''h虽然自身是Husky类型，但由于Husky是从Dog继承下来的，所以，h也还是Dog类型
即isinstance()判断的是一个对象是否是该类型本身，或者位于该类型的父继承链上
'''
print(isinstance(d,Animal))     # d也是Anima类型
print(isinstance(d,Husky))      # 但不是Husky类型


"""isinstance()函数还可以判断一个变量是否是某些类型中的一种"""
# 比如下面的代码就可以判断是否是list或者tuple：
print(isinstance([1,2,3],(list,tuple)))
print(isinstance((1,2,3),(list,tuple)))
print(isinstance((1,2,3),(list,dict)))