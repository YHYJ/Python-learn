#!/usr/bin/env python3
# -*- coding: utf-8 -*-


"""在one_one_.py中，类的属性会被外部代码访问修改

要让类内部属性不被外部访问，可以把属性的名称前加上两个下划线 ‘__’
Py中，实例的变量名如果以__开头，就变成了一个私有变量（private），只有内部可以访问
这样确保了外部代码不能随意修改对象内部的状态，这样通过访问限制的保护，代码更加健壮
"""

class Student():

    def __init__(self,name,score):
        self.__name = name
        self.__score = score

    def priint_score(self):
        print('%s：%s' % (self.__name,self.__score))

mark = Student(name='Mark',score=76)
mark.priint_score()
# print(mark.name)
# print(mark.__name)        # 已经无法从外部访问实例变量.__name和实例变量.__score


'''1、如果外部代码要获取name和age
可以给类增加get_name和get_score类似的方法
'''
'''2、允许外部代码修改age参数，并对参数做检查，避免传入无效的参数：
可以给类增加set_score类似方法
'''
# 1、给Teacher类增加get_name和get_age方法：
# 2、给Teacher类增加set_age方法：
class Teacher():

    def __init__(self,name,age):
        self.__name = name
        self.__age = age

    def priint_age(self):
        print("%s's age：%s" % (self.__name,self.__age))

    def get_name(self):
        '''使外部获得姓名'''
        return self.__name

    def get_age(self):
        '''使外部获得年龄'''
        return self.__age

    def set_age(self,age):
        '''使外部可修改age参数并对其进行检查'''
        if 0 <= age <= 150:
            self.__age = age
        else:
            raise ValueError('年龄错误')

amy = Teacher(name='Amy',age=22)
amy.priint_age()
print(amy.get_name())       # 外部代码调用get_name()方法获取name
amy.set_age(age=26)         # 允许外部代码修改age参数，但超出0~150将报错
print(amy.get_age())



'''
注意：在Py中，变量名类似__xxx__的，也就是以双下划线开头，并且以双下划线结尾的-
    -是特殊变量，特殊变量是可以直接访问的，不是private变量-
    -所以，不能用__name__、__score__这样的变量名

有时会看到以一个下划线开头的实例变量名，比如_name，这样的实例变量外部是可以访问的-
    -但按照约定俗成的规定，当看到这样的变量时，意思就是 —— 
        “虽然我可以被访问，但是，请把我视为私有变量，不要随意访问”
'''