#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""操作文件和目录的函数一部分放在os模块中，一部分放在os.path模块中"""

import os
import shutil
# shutil模块提供了copyfile()函数，可以看做是os模块的补充


file = open('./testdir/testfile.py', 'r+')

# 目录操作 ——查看、创建和删除目录
'''查看当前目录的绝对路径'''
print(os.path.abspath('.'))

'''在某个目录下创建一个新目录，首先把新目录的完整路径表示出来'''
print(os.path.join('.','testdir'))
'''然后创建目录(知道各系统路径分隔符可以直接创建不用join表示)'''
# os.mkdir(r'./testdir')  # 创建单层目录
# os.makedirs(r'./testdir/testdir1/testdir2')  # 创建多层目录

'''删除一个目录'''
# os.rmdir(r'./testdir')
# os.removedirs(r'./testdir/testdir1/testdir2')  # 删除多层目录

'''拆分路径'''
print(os.path.split('./testdir1'))
'''join(合并)、split(拆分)路径的函数并不要求目录和文件要真实存在
它们只对字符串进行操作'''


# 文件操作 ——重命名、删除、复制文件
'''查看文件编码格式'''
print('编码格式：', file.encoding)

'''查看文件名'''
print('文件名：', file.name)

'''查看文件权限'''
print('文件权限：', file.mode)

'''返回指定文件的绝对路径'''
print('本文件绝对路径：', os.getcwd())

'''判断指定文件是否存在'''
print(os.path.exists('操作文件和目录.py'))

'''得到文件扩展名'''
print(os.path.splitext('./__init__.py'))

'''重命名文件(目录也适用)'''
# os.rename('./testdir/file.txt','./testdir/testfile.py')

'''删除文件'''
# os.remove('./testdir/testfile.txt')

'''复制文件'''
# shutil.copyfile('./testdir/testfile.py', './test.py')
