#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""将自定义函数加入到猜数字小游戏"""


from random import randint


def judge(num1, num2):
    if num1 > num2:
        print('太小！')
        return False
    elif num1 < num2:
        print('太大！')
        return False
    else:
        print('猜对啦！！！')
        return True

if __name__ == '__main__':
    num = randint(0, 100)
    print('猜一个数字，在0~100之间！')
    start = False

    while start is False:
        answer = int(input('请输入你猜的数字：'))
        start = judge(num, answer)
    # eval(input('回车键以退出'))

'''在judge函数内部，会将num和answer进行对比-
-如果相等，就会将True返回给start，否则返回值False，循环继续'''
'''自定义函数可以将某个功能独立出来，在需要的时候就可以方便的进行调用'''
