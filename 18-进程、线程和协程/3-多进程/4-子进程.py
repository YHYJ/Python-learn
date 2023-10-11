#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""很多时候子进程并不是自身，而是一个外部进程
创建了子进程后，还需要控制子进程的输入和输出"""


import subprocess

"""subprocess模块可以非常方便地启动一个子进程，然后控制其输入和输出"""
# 在Py代码中运行命令nslookup www.python.org：

print("$ nslookup www.python.org")
r = subprocess.call(['nslookup', 'www.python.org'])
print("Exit code：",r)

print("*"*100)

# 如果子进程需要输入，则可以通过communicate()方法输入：
print("$ nslookup")
p = subprocess.Popen(['nslookup'], stdin=subprocess.PIPE,
                     stdout=subprocess.PIPE, stderr=subprocess.PIPE)
output, err = p.communicate(b'set q=mx\npython.org\nexit\n')
print(output.decode('utf-8'))
print("Exit code：", p.returncode)