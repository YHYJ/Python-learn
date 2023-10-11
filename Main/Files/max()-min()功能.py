#!/usr/bin/env python3
# -*- coding: utf-8 -*-


# max()
list_1 = [1000, 500, 2012, -954, 7800, 300, 2000]
maxli = list_1[0]
for i in list_1:
    if maxli <= i:
        maxli = i
print('最大值：', maxli)


# min()
list_1 = [1000, 500, 2012, -954, 7800, 300, 2000]
maxli = list_1[0]
for i in list_1:
    if maxli >= i:
        maxli = i
print('最小值：', maxli)
