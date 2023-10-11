#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""子类的__init__()中的super()__init__()
和方法中的super()__init__()区别"""


class Car(object):
    def __init__(self, age, lo):
        self.name = '父类15'
        self.age = age
        self.lo = lo

    def printf1(self):
        print(self.name)
        print(self.age)
        print(self.lo)


class Scar(Car):
    def __init__(self, agem):
        super().__init__(age='998', lo=12)  # 将父类的属性继承给子类，子类的方法可以调用父类的属性，需赋值age
        self.name = '子类16'
        self.agem = agem

    def printm(self):

        print(self.name)
        print(self.agem)
        print(self.age)

    def printf(self):
        super().__init__(age='mm', lo=34)  # 调用父类的__init__()，使用父类属性调用父类方法
        super().printf1()


c = Car(age='ff', lo=1)
c.printf1()

print('-------------------------')

s = Scar(agem='main')
s.printm()

print('-------------------------')

s.printf()
