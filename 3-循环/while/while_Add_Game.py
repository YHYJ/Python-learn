#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""把while加入到猜数字小游戏"""


num = 16
guess = True
print('猜一个数字，在0~100之间:')

while guess:
    answer = int(input('请输入你猜的数：'))

    if answer < num:
        print('太小了！')
        # print(answer)

    elif answer > num:
        print('太大了！')
        # print(answer)

    else:
        print('猜对了！！！')
        print('num =', answer)
        guess = False
