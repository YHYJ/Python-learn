#!/usr/bin/env python3
# -*- coding: utf-8 -*-


# 字符串
print('string')  # ===输出字符串用单引号===#
print("string")  # ===和双引号的效果一样===#


# Python可以将字符串赋给变量，然后通过变量输出字符串
str = 'hello'
print(str)


# 想要输出一段带有英文单引号或者双引号的字符串，有两种方法
# ======== 1、用另一种的引号类型 ========#
print("It's my way")
print('"Hero is never die"')
print()
# ======== 2、通过 转译字符\ ========#
print('It\'s my way')   # \' 表示单引号
print("\"英雄不朽\"")    # \" 表示双引号


# Python还有一种表示字符串的方法：三个引号(''')(""")
# 在三引号中可以 方便的使用 单引号 和 双引号 ，并且可以 直接换行
print('''
"What's your name?"I asked.
"I'm Li Lei."
''')   # 三单引号和三双引号一样

print()

# ======== 练习 ========#
# 1、输出He said,"I'm yours!"
print('He said,"I\'m yours!"')      # 用转译字符\搭配单引号
print("He said,\"I'm yours!\"")     # 用转译字符\搭配双引号
print('''He said,"I'm yours!"''')   # 用三单引号
print("""He said,"I'm yours!" """)  # 注意三双引号里的字符串如果结尾时一个双引号，这个双引号要和三双引号空开
print()
# 2、输出\\_V_//
print('\\\\_V_//')
print()
# 3、输出Stay hungry,
#      stay foolish,
#                   ——Steve Jobs
print('Stay hungry,')               # === 这是 ===#
print('stay foolish,')              # === 最笨 ===#
print('             ——Steve Jobs')  #=== 方法 ===#
print('Stay hungry,\nstay foolish,\n             ——Steve Jobs')  #=== 换行字符\n ===#
print('''Stay hungry,
stay foolish,
             ——Steve Jobs''')
print()
# 4、输出星菱形
print('''
   *
  ***
 *****
  ***
   *''')
