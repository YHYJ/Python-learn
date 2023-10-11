#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from random import choice   #choice——random的一个方法，作用是从一个list中随机挑选一个元素。也可以用randint来随机

score_you = 0
score_com = 0

print('点球大作战，进球吧！！！')
print('输入方向：左，中，右')
n = 1
while 1:
    print()
    print('第%d局'%n)
    you = input('选择你踢出的方向：')    #将‘左，中，右’三个字符任选一个赋给变量you，代表你踢出的方向
    print('你踢向了' + you)
    direction = ['左','中','右']   #定义一个list，元素为'左','中','右'
    com = choice(direction)     #通过choice从list direction中随机挑选一个元素赋给变量com
    print('守门员扑向了' + com)
    if you != com:              #如果你踢出的方向you不等于守门员扑向的方向，则球进
        print('球进啦！！！')
        score_you += 1  #玩家得分
    else:                       #反之球不进
        print('守门员一个完美的救球！！')
        score_com += 1  #门将得分
    print('得分：%d(你) —— %d(对方)'%(score_you,score_com))
    n += 1
    print()
    print('第%d局'%n)
    you = input('选择你防守的方向：')
    print('你防向了' + you)
    direction = ['左','中','右']
    com = choice(direction)
    print('对方踢向了' + com)
    if you != com:
        print('对面进球！！！')
        score_com += 1
    else:
        print('你一个完美的救球！！')
        score_you += 1
    print('得分：%d(你) —— %d(对方)'%(score_you,score_com))
    n += 1