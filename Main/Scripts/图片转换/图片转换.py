#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""转换图片的大小和类型"""

from PIL import Image

picture_path = input('输入图片绝对路径(类似/home/picture.png):')
im = Image.open(picture_path)
print('原图类型:', im.format)
print('原图尺寸:', str(im.size[0]) + '*' + str(im.size[1]))
print('原图模式:', im.mode)

picture_lsize = int(input('请输入目标图片的长度:'))
picture_wsize = int(input('请输入目标图片的宽度:'))
picture_mode = input('请输入目标图片的类型(jpg,png,bmp,):')
im.thumbnail((picture_lsize, picture_wsize))
if picture_mode == 'jpg':
    im.save('/home/yj/Pictures/Conversion_results.jpg', 'jpeg')
else:
    im.save('/home/yj/Pictures/Conversion_results.%s' % picture_mode,
            '%s' % picture_mode)
