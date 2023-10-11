#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""借用random模块，创建一个 Die 类.

包含一个名为 sides 的属性，该属性的默认值为 6.
编写一个名为 roll_die()的方法，它打印位于 1 和骰子面数之间的随机数.
创建一个 6 面的骰子，再掷 10 次。
创建一个 10 面的骰子和一个 20 面的骰子，并将它们都掷 10 次.
"""

from random import randint
#或者这样导入： import random ,使用randint时就是 random.randint()

class Die():
    """模拟骰子"""

    def __init__(self,sides = 6):
        """初始化属性sides"""
        self.sides = sides

    def rool_die(self):
        if self.sides == 6:
            return randint(1,6)
        elif self.sides == 10:
            return randint(1, 10)
        elif self.sides == 20:
            return randint(1, 20)

number6 = []
for x in range(10):
    guess = Die()
    number6.append(guess.rool_die())
print('6面骰子掷10次的结果：',number6)


number10 = []
for y in range(10):
    guess = Die(sides=10)
    number10.append(guess.rool_die())
print('10面骰子掷10次的结果：',number10)


number20 = []
for z in range(10):
    guess = Die(sides=20)
    number20.append(guess.rool_die())
print('20面骰子掷10次的结果：',number20)