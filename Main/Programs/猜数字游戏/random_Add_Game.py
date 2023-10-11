#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#把随机数模块加入到猜数字小游戏
from random import randint  #--from 模块名 import 方法名--#  #--或者这个写法：import random  #
num = randint(1,100)                                       #  num = random.randint(1,100)--#

guess = 0
print('猜一个数字，在0~100之间:')

while guess == 0:
    answer = int(input('请输入你猜的数：'))

    if answer < num:
        print('太小了！')
        #print(answer)

    elif answer > num:      #elif等效于C的else if，后面加条件
        print('太大了！')
        #print(answer)

    else:                  #else后面不能加条件
        print('猜对了！！！')
        print('num =',answer)
        guess = 1