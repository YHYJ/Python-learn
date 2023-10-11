#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Py的hashlib模块提供了常见的摘要算法，如MD5，SHA1等"""


import hashlib

"""摘要算法又称哈希算法、散列算法：
它通过一个函数，把任意长度的数据转换为一个长度固定的数据串
(通常用16进制的字符串表示)
"""
"""摘要算法就是通过摘要函数f()对任意长度的数据data计算出固定长度的摘要digest
目的是为了发现原始数据是否被人篡改过
"""
"""摘要算法之所以能指出数据是否被篡改过，是因为摘要函数是一个单向函数
计算f(data)很容易，但通过digest反推data却非常困难
而且,对原始数据做一个bit的修改，都会导致计算出的摘要完全不同
"""


# MD5算法——计算出一个字符串的MD5值
md5 = hashlib.md5()
md5.update('how to use md5 in python hashlib?'.encode('utf-8'))
print(md5.hexdigest())
md5.update('so how to use md5 in python hashlib?'.encode('utf-8'))
print(md5.hexdigest())
'''如果数据量很大，可以分块多次调用update()，最后计算的结果是一样的'''


# SHA1算法
sha1 = hashlib.sha1()
sha1.update('how to use md5 in python hashlib?'.encode('utf-8'))
print(sha1.hexdigest())
sha1.update('so how to use md5 in python hashlib?'.encode('utf-8'))
print(sha1.hexdigest())
'''SHA256和SHA512比SHA1更安全，不过越安全的算法不仅越慢，而且摘要长度更长'''
'''任何摘要算法都是把无限多的数据集合映射到一个有限的集合中。这种情况称为碰撞'''


# 摘要算法应用
'''确的保存口令的方式是不存储用户的明文口令，而是存储用户口令的摘要，比如MD5'''
'''当用户登录时，首先计算用户输入的明文口令的MD5，然后和数据库存储的MD5对比
如果一致，说明口令输入正确，如果不一致，口令肯定错误'''


# 加盐——通过对原始口令加一个复杂字符串来确保存储的用户口令不是那些已经被计算出来的常用口令的MD5
'''常用口令的MD5值很容易被计算出来c'''



print('*'*50 + ' work ' + '*'*50)
# ---------------- work ---------------- #
'''设计一个验证用户登录的函数，根据用户输入的口令是否正确，返回True或False'''
db = {
    'mich': 'e10adc3949ba59abbe56e057f20f883e',
    'bob': '878ef96e86145580c38c87f0410ad153',
    'alice': '99b1c2188db85afee403b1536010c2c9'
}

def login(user, password):
    md5_2 = hashlib.md5()
    md5_2.update(password.encode('utf-8'))    # 计算输入的密码的MD5值
    if md5_2.hexdigest() == db[user]:         # 比较输入的和存储的密码的MD5值是否相同
        return True
    else:
        return False

print('mich：123456\nbob:888888\nalice：password')
user = input('请输入用户名：')
password = input('请输入密码：')
print(login(user, password))



print('*'*50 + ' demo ' + '*'*50)
# ---------------- demo ---------------- #
'''读取文件，算出它的md5和sha1值'''
with open('/home/yj/Documents/Code/Py/3.5/各个常用模块及其简介/常用内建模块/file/hash.txt') as f:
    file = f.read()

    md5_1 = hashlib.md5()
    md5_1.update(file.encode('utf-8'))
    print(md5_1.hexdigest())
    sh1_2 = hashlib.sha1()
    sh1_2.update(file.encode('utf-8'))
    print(sh1_2.hexdigest())
