#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""多态
子类继承父类所有方法，并可以在自己的代码块中修改任意某个方法（假设为a()）-
-这样在运行a()时会调用子类修改后的a()方法
当定义一个名为Animal的类时，实际上定义了一种Animal数据类型，与Py自带的数据类型没有区别
在继承关系中，如果一个实例的数据类型是某个子类，那它的数据类型也可以被看做是父类。但是反过来就不行
"""


class Animal(object):
    """父类"""
    def run(self):
        print('Animal is running...')


class Dog(Animal):
    """子类"""
    def run(self):
        print('Dog is running...')

class Cat(Animal):
    """子类"""
    def run(self):
        print('Cat is running...')

class Tortoise(Animal):     # 对于类似Py的动态语言，不一定非要是Animal类型，只要他有run()方法就可以
    def run(self):
        print('Tortoise is running slowly...')

def run_twice(animal):
    animal.run()
    animal.run()

run_twice(Tortoise())

dog = Dog()
cat = Cat()
dog.run()
cat.run()
print(isinstance(dog,Dog))      # dog时Dog类型，也是Animal类型
print(isinstance(dog,Animal))
