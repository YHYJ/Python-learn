#!/home/yj/.virtualenvs/py3.5.3/bin/python3.5
# -*- coding: utf-8 -*-

"""对greet_user()函数进行重构,将它的任务进行拆分"""

import json

def get_stored_username():
    """如果用户名已存储，就获取它"""
    file_path = './Data/username.json'
    try:
        with open(file=file_path) as f_obj:
            username = json.load(f_obj)
    except FileNotFoundError:
        return None
    else:
        return username


def get_new_username():
    """提示用户输入用户名"""
    username = input("请输入用户名：")
    file_path = './Data/username.json'
    with open(file=file_path,mode='w') as f_obj:
        json.dump(username,f_obj)
    return username


def greet_user():
    """获得get_stored_username()函数的返回值，返回username则问候，None则创建用户"""
    username = get_stored_username()
    if username:    # 如果获得的返回值不是None
        print("欢迎回家，" + username)
    else:
        username = get_new_username()
        print("已创建用户 " + username)  # 创建完用户给予提示信息

greet_user()