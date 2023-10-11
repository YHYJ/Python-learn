#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
File: conver.py
Author: YJ
Email: yj1516268@outlook.com
Created Time: 2020-07-17 14:22:54

Description: 原码、反码、补码之间的转换

- 机器数：一个数在计算机中的二进制表示形式，叫做这个数的机器数。机器数是带符号的，在计算机用一个数的最高位存放符号，正数为0，负数为1
- 真值：因为第一位是符号位，所以机器数的形式值就不等于真正的数值。为区别起见，将带符号位的机器数对应的真正数值称为机器数的真值
    例：0000 0001的真值 = +000 0001 = +1，1000 0001的真值 = –000 0001 = –1
- 原码
    即一个数的真值的绝对值加上一个符号位
- 反码
    正数的反码是其本身
    负数的反码是在其原码的基础上保持符号位不变，其余位取反
- 补码
    正数的补码是其本身
    负数的补码是在其原码的基础上保持符号位不变，其余位取反，最后+1（即在反码的基础上+1）

"""


# 8位表示的界限
positive_8 = pow(2, 8 - 1) - 1
negative_8 = - positive_8


def conversion(number):
    """将参数number转换为其原码、反码、补码

    :number: TODO
    :returns: TODO

    """
    original_bin = 0b00000000       # 原码的二进制表示
    original_hex = 0x00             # 原码的十六进制表示
    inverted_bin = 0b00000000       # 反码的二进制表示
    inverted_hex = 0x00             # 反码的十六进制表示
    complementary_bin = 0b00000000  # 补码的二进制表示
    complementary_hex = 0x00        # 补码的十六进制表示
    # number是正数或零
    if number >= 0:
        # 二进制
        number_bin = bin(number)                        # 将number以二进制表示
        original_bin = number_bin[2:].zfill(8)          # 二进制以最少8位形式表示
        inverted_bin = complementary_bin = original_bin  # 反码和补码

        # 十六进制
        number_hex = hex(number)                        # 将number以十六进制表示
        original_hex = number_hex[2:].zfill(2)          # 十六进制以最少2位表示
        inverted_hex = complementary_hex = original_hex  # 反码和补码
    # number是负数
    #  else:
    #      number_abs = abs(number)                    # 求number的绝对值
    #
    #      # 二进制
    #      original_bin = bin(number_abs | )[2:]   # 对number的绝对值与 进行按位或操作以赋予其符号位

    print('{}的原码 = {} / {}'.format(number, original_bin, original_hex))
    print('{}的反码 = {} / {}'.format(number, inverted_bin, inverted_hex))
    print('{}的补码 = {} / {}'.format(number, complementary_bin, complementary_hex))


if __name__ == "__main__":
    conversion(100000)
