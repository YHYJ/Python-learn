#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""对一个能够以不同速度移动的外星人的位置进行跟踪.
存储该外星人的当前速度，并据此确定该外星人将向右移动多远
"""


ET = {'x': 0,'y': 25,'speed': 'medium'}
print('原位置坐标：(%d,%d)'%(ET['x'], ET['y']))

# 向右移动外星人
# 据外星人当前速度决定将其移动多远
if ET['speed'] == 'slow':   # 速度低
    x = 10
elif ET['speed'] == 'medium':   # 速度中等
    x = 20
else:
    # 速度高
    x = 30
ET['x'] = ET['x'] + x   # 新位置　＝　初始位置　+　移动距离
print('新位置坐标：(%d,%d)' % (ET['x'], ET['y']))
