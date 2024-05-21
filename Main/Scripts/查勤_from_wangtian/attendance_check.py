#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
File: attendance_check.py
Author: YJ
Email: yj1516268\\@outlook.com
Created Time: 2024-05-21 09:09:04

Description:
"""

import os

name_dict = dict.fromkeys(open('./name/names').readlines(), 0)
name_list_done = os.listdir('./') + os.listdir('name')

for name in name_dict:
    for j in name_list_done:
        if name.strip() in j:
            name_dict[name] += 1

unpassed = []
passed = []
for name, i in name_dict.items():
    if i == 0:
        unpassed.append(name.strip())
    else:
        for temp in range(i):
            passed.append(name.strip())
        if i > 1:
            print(name.strip())

print('没交还有:', len(unpassed), '人')
for i in unpassed:
    print(i, ' ', end='')
print()

print('交了:', len(passed))
for i in passed:
    print(i, ' ', end='')
