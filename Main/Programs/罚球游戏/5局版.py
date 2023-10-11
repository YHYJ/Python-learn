#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from random import choice   #choice——random的一个方法，作用是从一个list中随机挑选一个元素。也可以用randint来随机

score = [0,0]
direction = ['左', '中', '右']  # 定义一个list，元素为'左','中','右'

print('点球大作战！！！')
print('输入方向：左，中，右')

def game():
    print('     == 进 攻 ==   ')
    you = input('选择你踢出的方向：')    #将‘左，中，右’三个字符任选一个赋给变量you，代表你踢出的方向
    print('你踢向了' + you)
    com = choice(direction)     #通过choice从list direction中随机挑选一个元素赋给变量com
    print('守门员扑向了' + com)
    if you != com:              #如果你踢出的方向you不等于守门员扑向的方向，则球进
        print('球进啦！！！')
        score[0] += 1  #玩家得分
    else:                       #反之球不进
        print('守门员一个完美的救球！！')
    print('得分：%d(你) —— %d(守)'%(score[0],score[1]))

    print('     == 防 守 ==   ')
    you = input('选择你防守的方向：')
    print('你守向了' + you)
    com = choice(direction)
    print('对方踢向了' + com)
    if you != com:
        print('球进了！！！')
        score[1] += 1
    else:
        print('你一个完美的救球！！')
    print('得分：%d(你) —— %d(守)' % (score[0], score[1]))

for i in range(1,3):
    print()
    print('======= 第%d局 ======='%i)
    game()

while score[0] == score[1]:
    i += 1
    print()
    print('======= 加 时 =======')
    print('     == 进 攻 ==')
    you = input('选择你踢出的方向：')
    print('你踢向了' + you)
    com = choice(direction)
    print('守门员扑向了' + com)
    if you != com:
        print('球进啦！！！')
        score[0] += 1
    else:
        print('守门员一个完美的救球！！')
    print('得分：%d(你) —— %d(守)' % (score[0], score[1]))

if score[0] > score[1]:
    print('你赢了！！！')
else:
    print('你输了。')