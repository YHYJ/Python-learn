#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Dog     -狗
Bat     -蝙蝠
Parrot  -鹦鹉
Ostrich -鸵鸟
把这四种动物分成：
‘哺乳类’ ——
    -‘能跑的’
    -‘能飞的’
‘鸟类’ ——
    -‘能跑的’
    -‘能飞的’
    
如果要再增加“宠物类”和“非宠物类”等等，类的数量会呈指数增长，很明显这样设计是不行的
正确的做法是采用多重继承"""
# 首先，主要的类层次仍按照哺乳类和鸟类设计：
class Animal():
    pass

# 一级类 —— ‘哺乳类‘ 和 ‘鸟类’
class Mammal(Animal):
    """哺乳类"""
    pass

class Bird(Animal):
    """鸟类"""
    pass

# 二级类 —— ’能跑的‘ 和 ’能飞的‘
class RunnableMixIn():
    """能跑的"""
    def run(self):
        print('They can Running...')

class FlyableMixIn():
    """能飞的"""
    def fly(self):
        print('They can Flying...')


# 各种动物
class Dog(Mammal,RunnableMixIn):
    """狗 —— 哺乳类，能跑"""
    pass

class Bat(Mammal,FlyableMixIn):
    """蝙蝠 —— 哺乳类，能飞"""
    pass

class Parrot(Bird,FlyableMixIn):
    """鹦鹉 —— 鸟类，能飞"""
    pass

class Ostrics(Bird,RunnableMixIn):
    """鸵鸟 —— 鸟类，能跑"""
    pass
'''通过多重继承，一个子类就可以同时获得多个父类的所有功能'''
'''在设计类的继承关系时，通常，主线都是单一继承下来的 ——
    例如，Ostrich继承自Bird
    但是，如果需要“混入”额外的功能，通过多重继承就可以实现-
    -比如，让Ostrich除了继承自Bird外，再同时继承Runnable
    这种设计通常称之为 —— MixIn

为了更好地看出继承关系，把Runnable和Flyable改为RunnableMixIn和FlyableMixIn
类似的，还可以定义出肉食动物CarnivorousMixIn和植食动物HerbivoresMixIn-
-让某个动物同时拥有好几个MixIn
'''
'''MixIn的目的就是给一个类增加多个功能 ——
    这样在设计类的时候，优先考虑通过多重继承来组合多个MixIn的功能-
    -而不是设计多层次的复杂的继承关系

Py自带的很多库也使用了MixIn ——
    例如，Py自带了TCPServer和UDPServer这两类网络服务-
    -而要同时服务多个用户就必须使用：
        多进程(ForkingMixIn)
        多线程(ThreadingMixIn)
        协程(CoroutineMixIn)
    模型
    通过组合就可以创造出合适的服务来
'''

'''Py允许使用多重继承，因此MixIn是一种常见的设计
只允许单一继承的语言（如Java）不能使用MixIn的设计
'''