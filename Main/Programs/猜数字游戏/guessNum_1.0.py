#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import random

secret = random.randint(1,100)  #选一个随机数
guess = 0   #玩家猜的数
tries = 0   #猜测次数

print ('请猜一个数字！')
print ('该数字为1~99的其中一个！你有6次猜测机会！！')

while guess != secret and tries < 7:    #最多允许猜6次
    guess = int(input('你猜的数字是：'))    #得到玩家猜的数
    if guess < secret:
        print('太低了!')
    elif guess > secret:
        print('太高了！')
    tries = tries ++ 1  #用掉一次机会
    if guess == secret:
        print('恭喜你，猜对了！！！')
else:
    print('游戏机会已用完，下次好运！ :-D')
    print('这个随机数是：',secret)
