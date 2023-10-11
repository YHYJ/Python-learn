#!/usr/bin/env python3
# -*- coding: utf-8 -*-

dic = {'a': 1, 'b': 2, 'c': 3}

# 默认迭代key：
for d in dic:
    print(d)


print("*"*50)

# 迭代value：
for dic_v in dic.values():
    print(dic_v)


print("*"*50)

# 同时迭代key和value：
for x,y in dic.items():
    print(x,'=',y)
