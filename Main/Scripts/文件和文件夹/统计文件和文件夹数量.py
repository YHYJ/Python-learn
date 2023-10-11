#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""统计指定目录下文件和文件夹数量"""

import os


path = input("路径：")
file_num = 0    # 文件数
folder_num = 0  # 文件夹数


def alter(path):
    global file_num
    global folder_num
    
    for file in os.listdir(path):
        if os.path.isdir(path + os.sep + file):     # 如果是文件夹
            print('<文件夹>：', path + os.sep + file)
            folder_num += 1
            alter(path + os.sep + file)
        else:    # 如果是普通文件
            print('<文件>', path + os.sep + file)
            file_num += 1
    return file_num, folder_num


file_num, folder_num = alter(path)
print("\n\n[info]：统计完成")
print("<总文件数>：%d\n<文件夹数>：%d" % (file_num, folder_num))

