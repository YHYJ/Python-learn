#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pygame
from sys import exit


def main():

    pygame.init()
    big = pygame.display.set_mode((960, 640), 0, 32)    # 创建窗口，设置大小
    pygame.display.set_caption('Mccree')  # 程序标题
    file = pygame.image.load('./data/Mccree.jpg')  # 创建填充图片

    while True:
        for picture in pygame.event.get():
            if picture.type == pygame.QUIT:
                pygame.quit()
                exit()
            big.blit(file, (0, 0))
            pygame.display.update()

if __name__ == '__main__':
    main()
