#!/home/yj/.virtualenvs/py3.5.3/bin/python3.5
# -*- coding: utf-8 -*-

"""保存和读取用户生成的数据"""

import json

# 如果以前存储了用户名，就加载它，否则就提示用户输入用户名并存储它
file_path = './Data/username.json'
try:
    with open(file=file_path) as f_obj:
        user_name = json.load(f_obj)
except FileNotFoundError:   # 首次运行这个程序时，文件username.json不存在
    user_name = input("请创建用户名：")
    with open(file=file_path,mode='w') as f_obj:
        json.dump(user_name,f_obj)  # 使用json.dump()存储该用户名
        print("已创建用户 " + user_name)
else:
    print("欢迎回家，" + user_name)