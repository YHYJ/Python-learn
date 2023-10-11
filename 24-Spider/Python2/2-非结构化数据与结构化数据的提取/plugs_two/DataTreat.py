#!/usr/bin/env python3
# -*- coding: utf-8 -*-


class DataTreat:
    """正则数据处理"""
    def __init__(self, data, pattern, pattern_content):
        self.data = data    # 参数传进来的待处理数据
        self.pattern = pattern  # 模糊匹配数据的 Pattern 对象
        self.pattern_content = pattern_content  # 除去剩下的无用数据的 Pattern 对象

    def treat(self):
        """初次数据处理"""
        data_list = self.pattern.findall(self.data)
        return data_list

    def treat_two(self, data):
        """最终数据处理"""
        ultimate_data = self.pattern_content.sub("", data)
        return ultimate_data
