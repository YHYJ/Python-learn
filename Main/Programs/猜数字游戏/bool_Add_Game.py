#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#把bool加入到猜数字小游戏
num = 16;
print('猜一个数字，在0~100之间:')
answer = int(input('请输入你猜的数：'))

if answer < num:
    print('太小了！')
    #print(answer)

elif answer > num:      #elif等效于C的else if，后面加条件
    print('太大了！')
    #print(answer)

else:       #else后面不能加条件
    print('猜对了！！！')
    print('num =',answer)