#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#把bool加入到猜数字小游戏
#把while加入到猜数字小游戏
#把随机数模块加入到猜数字小游戏
#把字符串格式化加入到猜数字小游戏
# -*- coding: utf-8 -*-
from random import randint  #===或者这个写法：import random===#
num = randint(1,100)        #===num = random.randint(1,100)#

guess = False
print('猜一个数字，范围是0~100！')

while guess == False:
    answer = int(input('请输入你猜的数字：'))

    if answer < num:
        print('%d 太小！'%answer)
        #print(answer)

    elif answer > num:      #elif等效于C的else if，后面加条件
        print('%d 太大！'%answer)
        #print(answer)

    else:                  #else后面不能加条件
        print('恭喜猜对！！！')
        print('这个数字是 %d'%answer)
        guess = True
    if answer < 0:
        print('即将退出游戏！')
        break
#eval(input('回车键退出'))