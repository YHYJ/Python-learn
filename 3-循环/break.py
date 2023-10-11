#!/usr/bin/env python3
# -*- coding: utf-8 -*-


"""break和continue，其改变的仅仅是当前所处的最内层循环的运行
如果外层还有循环，并不会因此略过或跳出
"""


# break      ——彻底跳出 本层 循环
# continue   ——在本层循环中略过 本次循环 的 余下的 内容，进入下一循环


i = 0
while i < 5:
    i += 1
    for j in range(3):
        print(j)
        if j == 2:
            break
    for k in range(3):
        if k == 2:
            continue
        print(k)
    if i > 3:
        break   # i=3以后，跳出这层循环，所以i只到3
    print(i)


li = ['Bart', 'Lisa', 'Adam']
for num in li:
    print('Hello,', num)
