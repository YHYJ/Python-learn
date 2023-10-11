#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Py提供struct模块来解决bytes和其他二进制数据类型的转换"""

import struct


'''准确地讲，Py没有专门处理字节的数据类型
但由于b'str'可以表示字节，所以字节数组＝二进制str
C语言中可以很方便地用struct、union来处理字节，以及字节和int，float的转换
'''

# Py中，比如要把一个32位无符号整数变成字节，也就是4个长度的bytes
'''要配合位运算符这么写'''
n = 10240099
b1 = (n & 0xff000000) >> 24
b2 = (n & 0xff0000) >> 16
b3 = (n & 0xff00) >> 8
b4 = (n & 0xff)
bs = bytes([b1, b2, b3, b4])
print(bs)
'''非常麻烦。如果换成浮点数就无能为力了'''


# Py提供了一个struct模块来解决bytes和其他二进制数据类型的转换
'''pack函数把任意数据类型变成bytes'''
bt = struct.pack('>I', 10240099)    # '>I' ——处理指令
''' > 表示字节顺序是big-endian(网络序)， I 表示4字节无符号整数'''
print(bt)

'''unpack函数吧bytes变成相应的数据类型'''
unbt = struct.unpack('>IH', b'\xf0\xf0\xf0\xf0\x80\x80')
'''根据>IH，后面的bytes依次变为I：4字节无符号整数和H：2字节无符号整数'''
print(unbt)


# Windows的位图文件（.bmp）是一种非常简单的文件格式
'''BMP格式采用小端方式存储数据，文件头的结构按顺序如下：
两个字节：'BM'表示Windows位图，'BA'表示OS/2位图
一个4字节整数：表示位图大小；      I——4字节  
一个4字节整数：保留位，始终为0；    I——4字节
一个4字节整数：实际图像的偏移量；   I——4字节
一个4字节整数：Header的字节数；    I——4字节
一个4字节整数：图像宽度；          I——4字节
一个4字节整数：图像高度；          I——4字节
一个2字节整数：始终为1；           H——2字节
一个2字节整数：颜色数；            H——2字节
'''
s = b'\x42\x4d' \
    b'\x38\x8c\x0a\x00\x00\x00\x00\x00\x36\x00\x00\x00' \
    b'\x28\x00\x00\x00\x80\x02\x00\x00\x68\x01\x00\x00' \
    b'\x01\x00\x18\x00'
uns = struct.unpack('<ccIIIIIIHH', s)
print(type(uns), uns)
'''输出：(b'B', b'M', 691256, 0, 54, 40, 640, 360, 1, 24)
b'B', b'M' 说明是win位图，位图大小640*360，颜色数为24
'''


# struct模块定义的数据类型可以参考Py官方文档：
'''https://docs.python.org/3/library/struct.html#format-characters'''


print('*'*50 + ' work ' + '*'*50)
"""检查任意文件是否是位图文件，如果是，打印出图片大小和颜色数"""
def work(filename):
    with open(filename, 'rb') as f:
        file = f.read(30)
        byte = struct.unpack('<ccIIIIIIHH', file)
        assert byte[0]==b'B' and byte[1]==b'M', '非位图文件'
        print(byte)
        print('文件类型：位图  图片规格：(%s,%s) 颜色数：%s' % (byte[6], byte[7], byte[-1]))

if __name__ == '__main__':
    work('/home/yj/Documents/Code/Py/3.5/Program/alien_invasion/file/images/ship.bmp')
