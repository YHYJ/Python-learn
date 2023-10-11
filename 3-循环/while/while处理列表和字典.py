#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""要在遍历列表的同时对其进行修改，可使用while循环.
通过将while循环同列表和字典结合起来使用，
可收集、存储并组织大量输入，供以后查看和显示.
"""


print("*"*25 + "在列表之间移动元素" + "*"*25)

'''在列表之间移动元素.

假设有一个列表，其中包含新注册但还未验证的网站用户；
使用一个while循环，在验证用户的同时将其从未验证用户列表中提取出来，
再将其加入到另一个已验证用户列表中.
'''
# 首先创建一个待验证用户列表
# 和一个用来存储已验证用户的空列表
un_users = ['1516', '妖君', 'YJ', 'YJ1516']
users = []

# 验证每个用户，直到没有未验证用户
# 将每个经过验证的用户移到已验证用户列表
while un_users:
    user = un_users.pop()   # 依次删除un_users末尾未验证的用户并存储到变量user

    print("正在验证用户：" + user.title())     # 提示正在验证的信息
    users.append(user)      # 将验证完成的用户添加到已验证用户列表

# 显示所有已验证的用户
print("\n已通过验证用户：")
for my_users in users:
    print(my_users.title())


print("*"*25 + "删除列表中所有的指定元素" + "*"*25)

'''删除列表中所有的指定元素.

remove()可以删除列表中特定值.
'''
pets = ['dog', 'cat', 'dog', 'goldfish', 'cat', 'rabbit', 'cat']
print(pets)

while 'cat' in pets:    # 检查列表pets中是否还有 'cat' 元素
    pets.remove('cat')
print(pets)


print("*"*25 + "使用用户输入填充字典" + "*"*25)

'''可使用while循环来提示用户输入任意数量的信息.

调查程序，其中的循环每次执行时都提示输入被调查者的名字和回答并存储到字典.
'''
responses = {}

# 设置标志
value = True

while value:
    # 提示被调查者输入名字和回答
    name = input("你的名字是：")
    response = input("你最喜欢星期几？你的答案是：")

    # 将答卷按照名字存储到字典中
    responses[name] = response

    # 看是否还有人要参与调查
    repat = input("请问你要参与其他调查么？（是/否）")
    if repat == '否':
        value = False

# 调查结束，显示结果
print("-"*10 + "调查结果" + "-"*10)
for name, response in responses.items():
    print(name + "\t" + "最喜欢的是 " + "\t" + response + ".")
