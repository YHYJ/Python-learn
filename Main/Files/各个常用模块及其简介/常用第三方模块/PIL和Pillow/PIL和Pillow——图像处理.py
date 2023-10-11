#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""PIL：Python Imaging Library，已经是Py平台事实上的图像处理标准库了
PIL功能非常强大，但API却非常简单易用，但仅支持到Py 2.7，且年久失修
一群志愿者在PIL的基础上创建了兼容的版本，名叫Pillow
支持最新Py 3.x，又加入了许多新特性
"""

from PIL import Image, ImageFilter, ImageDraw, ImageFont
import random


# 操作图像
'''图像缩放'''
im = Image.open('./data/Mccree.jpg')    # 打开一个jpg图像文件
w, h = im.size      # 获得图像尺寸
print('图像尺寸：%s x %s' % (w, h))
im.thumbnail((w//2, h//2))        # 缩放到50%，参数类型为元组
print('缩放图片：%s x %s' % (w//2, h//2))
im.save('./data/缩放Mccree.jpg', 'jpeg')    # 把缩放后的图像用jpeg格式保存

'''模糊效果'''
im_1 = im.filter(ImageFilter.BLUR)
im_1.save('./data/模糊Mccree.jpg', 'jpeg')


# 直接绘图——PIL的ImageDraw提供了一系列绘图方法，让我们可以直接绘图
'''生成字母验证码图片'''
def rnd_char():
    '''生成随机字母'''
    return chr(random.randint(65, 90))

def rnd_color_1():
    '''随机颜色1'''
    return (random.randint(64, 255), random.randint(67,255), random.randint(67,255))

def rnd_color_2():
    '''随机颜色2'''
    return (random.randint(32, 127), random.randint(32, 127), random.randint(32, 127))

width = 60 * 4  # 尺寸
height = 60
image = Image.new('RGB', (width, height), (255, 255, 255))
font = ImageFont.truetype('/usr/share/fonts/truetype/deepin/DeepinOpenSymbol5.ttf', 36)  # 创建font对象
draw = ImageDraw.Draw(image)                # 创建draw对象
# 填充每个元素
for x in range(width):
    for y in range(height):
        draw.point((x, y), fill=rnd_color_1())
# 输出文字
for t in range(4):
    draw.text((30 * t + 10, 10), rnd_char(), font=font, fill=rnd_color_2())
# 模糊处理
image = image.filter(ImageFilter.BLUR)
image.save('./data/code.jpg', 'jpeg')