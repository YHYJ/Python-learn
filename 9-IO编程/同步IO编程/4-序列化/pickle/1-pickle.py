#!/home/yj/.virtualenvs/py3.5.3/bin/python3.5
# -*- coding: utf-8 -*-


"""Py提供pickle模块实现序列化"""
import pickle
d = dict(name='Bob',age='20',score='76')
# pickle.dumps()方法把任意对象序列化成一个bytes，可以把这个bytes写入文件：
print(pickle.dumps(d))
# 或者使用pickle.dump()直接把对象序列化后写入一个file-like Object：
with open(file='./Data/dump.txt', mode='wb') as f:
    pickle.dump(d, f)


"""反序列化刚才保存的对象"""
with open('./Data/dump.txt', 'rb') as fr:
    dr = pickle.load(fr)
    print(dr)
'''变量 dr 和原来的变量 d 是完全不相干的对象，它们只是内容相同而已'''



"""Pickle的问题和所有其他编程语言特有的序列化问题一样 —— 它只能用于Py
并且可能不同版本的Py彼此都不兼容
因此只能用Pickle保存那些不重要的数据，不能成功地反序列化也没关系"""