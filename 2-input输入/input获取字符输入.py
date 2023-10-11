#!/usr/bin/env python3
# -*- coding: utf-8 -*-


"""input()的工作原理
input()使程序暂停运行等待用户输入
"""

message = input("复读机： ")     # 提示用户输入的内容
print(message)


prompt = "如果告诉我你是谁，我也不会知道我会干什么\n请输入你的名字：　"
name = input(prompt)
print("Hello," + name)
