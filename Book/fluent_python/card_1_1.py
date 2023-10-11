#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Author: YJ
Email: yj1516268@outlook.com
Created Time: 2019-03-18 16:31:21

__len__、__getitem__
TODO: 洗牌功能
"""

import collections

from random import choice

Card = collections.namedtuple('Card', ['rank', 'suit'])  # 表示一张纸牌


class FrenchDeck:
    """一摞有序的纸牌.
    FrenchDeck隐式继承了基类object,但功能并非继承而来.
    功能通过数据模型和一些合成来实现，通过实现__len__和__getitem__这两个特殊方法，
    FrenchDeck就跟一个Python自由的序列数据类型一样可以体现出Python的核心语言特性（
    例如迭代和切片）.
    """

    ranks = [str(n) for n in range(2, 11)] + list('JQKA')  # 牌面
    suits = 'spades diamonds clubs hearts'.split()  # 花色

    def __init__(self):
        """对合成的运用使得__len__和__getitem__的具体实现
        可以代理给self._cards这个list对象.
        """
        self._cards = [
            Card(rank, suit) for rank in self.ranks for suit in self.suits
        ]

    def __len__(self):
        """TODO: Docstring for __len__.
        :returns: TODO

        """
        return len(self._cards)

    def __getitem__(self, position):
        """TODO: Docstring for __getitem__.

        :position: TODO
        :returns: TODO

        __getitem__方法使得:
            []操作交给了self._cards列表，所以FrenchDeck类自动支持切片
            Card可迭代
        """
        return self._cards[position]


def spades_high(card):
    """排序
    2最小，A最大；黑桃最大，红桃次之，方块再次，梅花最小
    所以最小的梅花2权重是0，最大的黑桃A权重是51

    :card: TODO
    :returns: TODO

    """
    suit_values = dict(spades=3, hearts=2, diamonds=1, clubs=0)  # 花色权重

    rank_value = FrenchDeck.ranks.index(card.rank)
    return rank_value * len(suit_values) + suit_values[card.suit]


cards = FrenchDeck()

print("-----------------------FrenchDeck-----------------------")
print(len(cards))
print(cards[1])
print(choice(cards))  # 从非空序列随机选择一个元素
print(cards[12::13])  # 切片
for card in cards:  # 迭代
    print(card)
print(Card('Q', 'hearts') in cards)  # 虽然没有实现__contains__方法，但in运算符可以做一次迭代搜索

print("-----------------------spades_high-----------------------")
for card in sorted(cards, key=spades_high):  # 排序
    print(card)
