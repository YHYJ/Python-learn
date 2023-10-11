#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = '1516 YJ'

"""模块搜索路径:
当试图加载一个模块时,Py会在指定的路径下搜索对应的.py文件,
如果找不到,就会报错找不到该模块
默认情况下,Py解释器会搜索 ——
    当前目录
    所有已安装的内置模块
    第三方模块
"""
# 搜索路径存放在sys模块的path变量中:
import sys

print(sys.path)


"""如果要添加自己的搜索目录,有两种方法"""
# 一、直接修改sys.path，添加要搜索的目录：
sys.path.append('/home/yj/Documents/code')  # 运行时修改，运行结束后失效
# 二、设置环境变量PYTHONPATH：
# 该环境变量的内容会被自动添加到模块搜索路径中
# 设置方式与设置Path环境变量类似
# 注意只需要添加自己的搜索路径
# Python自己本身的搜索路径不受影响
