#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""遍历多层目录，更改文件(666)和文件夹(755)的权限"""

import os
import stat as s

'''
s.S_IRUSR|s.S_IWUSR|s.S_IXUSR     # 设置U权限
s.S_IRGRP|s.S_IWGRP|s.S_IXGRP     # 设置G权限
s.S_IROTH|s.S_IWOTH|s.S_IXOTH     # 设置O权限
'''


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
            os.chmod(path + os.sep + file,
                     s.S_IRUSR | s.S_IWUSR | s.S_IXUSR |
                     s.S_IRGRP | s.S_IXGRP |
                     s.S_IROTH | s.S_IXOTH)         # 文件夹权限755
            alter(path + os.sep + file)
        else:    # 如果是普通文件
            print('<文件>', path + os.sep + file)
            file_num += 1
            os.chmod(path + os.sep + file,
                     s.S_IRUSR | s.S_IWUSR |
                     s.S_IRGRP | s.S_IWGRP |
                     s.S_IROTH | s.S_IWOTH)         # 文件权限666
    return file_num, folder_num


file_num, folder_num = alter(path)
print("\n\n[info]：权限修改完成")
print("<总文件数>：%d\n<文件夹数>：%d" % (file_num, folder_num))

