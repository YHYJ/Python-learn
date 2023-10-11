#!/home/yj/.virtualenvs/py3.5.3/bin/python3.5
# -*- coding: utf-8 -*-

"""对remember_me.py进行重构,将大部分逻辑放到greet_user()函数中"""

import json

def greet_user():
    """问候用户，并指出其名字"""
    file_path = './Data/username.json'
    try:
        with open(file=file_path) as f_obj:
            username = json.load(f_obj)
    except FileNotFoundError:
        username = input("请创建用户名：")
        with open(file=file_path,mode='w') as f_obj:
            json.dump(username,f_obj)
            print("已创建用户 " + username)
    else:
        print("欢迎回家，" + username)

greet_user()