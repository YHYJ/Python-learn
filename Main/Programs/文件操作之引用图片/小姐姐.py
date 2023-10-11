#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pygame   # 导入pygame库
from sys import exit    # 向sys模块借一个exit函数用来退出程序


def main():

    pygame.init()   # 初始化pygame，为使用硬件做准备
    screen = pygame.display.set_mode((1920, 1043), 0, 8)  # 窗口规格，图片质量——数值(8~32)
    pygame.display.set_caption('小姐姐')   # 设置窗口标题
    background = pygame.image.load('./data/小姐姐.jpg').convert()  # 加载并转换图像。.convert注释也不报错？？

    while True:  # 游戏主循环
        for event in pygame.event.get():
            if event.type == pygame.QUIT:   # 接收到退出事件后退出程序
                pygame.quit()
                exit()
            screen.blit(background, (0, 0))   # 将背景图画上去
            pygame.display.update()  # 刷新一下画面

if __name__ == '__main__':
    main()
