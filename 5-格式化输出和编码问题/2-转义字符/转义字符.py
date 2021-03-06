#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#======== 转译字符\的用法 ========#
# 1、用来表示引号等特殊符号
print("I\'m a \"good\" teacher")
print('输出自身：\\')

# 2、字符串中的换行
print("换行\n在这")

# 3、用来在代码中换行而不影响输出的结果
print('代码都写在这一行就太长了，但是\
我想要输出的结果是这行字都在一行上，就可以这样！')

# 4、制表符
print('1516\tA\t袅袅娜娜')   #缩进

# 5、如果字符串里面有很多字符都需要转义，就需要加很多\，为了简化，Python还允许用r''表示''内部的字符串默认不转义：
print(r'\t1516\t')
print(r"""1\n
2\t4
3""")
