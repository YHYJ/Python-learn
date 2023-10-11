#!/usr/bin/env python3
# -*- coding: utf-8 -*-

""""""


score = {
    '萧峰': 95,
    '段誉': 97,
    '虚竹': 89,
    '1': 123,
    '2': 456,
    '1516': 100,     # 在最后一个键—值对后面也加上逗号，为在下一行添加键—值对做好准备。
    }


# 字典的拷贝
new_score = score.copy()    # 深拷贝


# 删除一项字典项的4种方法
'''del：
彻底删除'''
del(score['虚竹'])
print(score, '\n')

'''pop(key)：
 如果键存在，返回其值，不存在默认报错，但第二个参数可以指定返回值'''
for name in score:
    print(name, score[name])
score.pop('1516', '无')   # 还可通过将score.pop('1516')赋值给一个变量来访问删除的字典项
print(score, '\n')

'''popitem()
从后向前删除，并返回该键值对元组形式'''
print(score)
print(score.popitem())
print(score, '\n')

'''clear()
清空字典元素，但不删除字典本身'''
print(score)
print(score.clear())
print(score)
