#!/usr/bin/env python3
# -*- coding: utf-8 -*-

""""""


score = {
    '萧峰': 95,
    '段誉': 97,
    '虚竹': 89,
    '1516': 100,
}

score_1 = {
    '萧峰': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}

# update()
'''完全用参数里的字典替换被操作字典'''
print(score)
score.update(score_1)
print(score)
'''两个字典都有的键就替换，被更新字典没有的键就增加'''
