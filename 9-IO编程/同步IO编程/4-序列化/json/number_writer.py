#!/home/yj/.virtualenvs/py3.5.3/bin/python3.5
# -*- coding: utf-8 -*-

"""把Py对象变成一个JSON以存储数据"""

import json

# dumps()方法返回一个str，内容就是标准的JSON：
d = dict(name='Mark',age=21,score=67)
print(json.dumps(d))


# dump()方法直接把JSON写入一个file-like Object：
numbers = [2,3,5,7,11,13,'A','a','妖君']
file_path = './Data/numbers.json'
with open(file=file_path, mode='w') as f_obj:
    json.dump(numbers,f_obj)
