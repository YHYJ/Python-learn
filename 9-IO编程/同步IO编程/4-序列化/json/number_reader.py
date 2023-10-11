#!/home/yj/.virtualenvs/py3.5.3/bin/python3.5
# -*- coding: utf-8 -*-

"""把JSON反序列化为Py对象"""

import json

# json.loads()把JSON的字符串反序列化
json_str = '{"age":21, "name":"Mark", "score":67}'
print(json.loads(json_str))


# json.load()从file-like Object中读取字符串并反序列化
file_path = './Data/numbers.json'
with open(file=file_path) as f_obj:
    numbers = json.load(f_obj)
    print(numbers)