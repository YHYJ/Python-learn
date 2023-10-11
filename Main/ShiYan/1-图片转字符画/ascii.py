#!/usr/bin/env python3

import argparse
from PIL import Image


"""argparse模块负责处理命令行参数"""


# 处理命令行输入的参数
parser = argparse.ArgumentParser()
parser.add_argument('file')     # 输入文件
parser.add_argument('-o', '--output')   # 输出文件
parser.add_argument('--width', type=int, default=80)    # 输出字符的宽度，默认80
parser.add_argument('--height', type=int, default=80)   # 输出字符的高度，默认80

# 获取参数
args = parser.parse_args()
IMG = args.file
WIDTH = args.width
HEIGHT = args.height
OUTPUT = args.output

# 字符画使用的字符集
ascii_char = list("$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'. ")


def get_char(r, g, b, alpha=255):
    """RGB值转字符，将256灰度映射到 ascii_char 的70个字符上"""
    if alpha is 0:
        return ' '
    length = len(ascii_char)    # 70
    gray = int(0.2126 * r + 0.7152 * g + 0.0722 * b)    # 灰度值公式
    unit = (256.0 + 1)/length

    return ascii_char[int(gray/unit)]


if __name__ == '__main__':
    im = Image.open(IMG)
    im = im.resize((WIDTH, HEIGHT), Image.NEAREST)

    txt = ""

    for i in range(HEIGHT):
        for j in range(WIDTH):
            txt += get_char(*im.getpixel((j, i)))
        txt += '\n'

    print(txt)

    # 将字符画输出到文件
    if OUTPUT:
        with open(OUTPUT, 'w') as f:
            f.write(txt)
    else:
        with open("output.txt", 'w') as f:
            f.write(txt)
