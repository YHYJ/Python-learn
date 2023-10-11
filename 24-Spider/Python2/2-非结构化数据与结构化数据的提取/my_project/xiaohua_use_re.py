#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""'http://www.neihan8.com/article/list_5_{}.html'.format(page_num)"""

import re

from plugs_two import xiaohua_info
from plugs_two.Spider import Spider
from plugs_two.DataTreat import DataTreat
from plugs_two.Save import SaveData


def xh_spider():
    """抓取数据"""
    param = xiaohua_info()
    de_code = param["de_code"]
    a_page = param["a_page"]
    e_page = param["e_page"]
    filename = param["filename"]

    raw_input("<INFO> 检查代码，回车执行")

    for page in range(a_page, e_page + 1):
        url = "http://www.neihan8.com/article/list_5_{}.html".format(page)
        spider = Spider(de_code)
        data = spider.send_request(url)

        """数据处理"""
        pattern = re.compile(r'<div class="f18 mb20">(.*?)</div>',
                             re.S)  # re.S表示启用DOTALL模式，让.也可以匹配换行符
        pattern_content = re.compile(r"<.*?>|&.*?;|\s|　")
        '''匹配网页里的无用字符
            <> 表示匹配标签 <p> <br>
            &.*?; 表示HTML实体字符
            \s 表示英文的空白字符 \n
            　:表示 \u3000 全角空格
        '''

        data_tread = DataTreat(data, pattern, pattern_content)  # 数据处理类对象

        print("<INFO> 过滤数据ing...")
        data_list = data_tread.treat()   # 第一道处理手续

        no_saved_data = []
        print("<INFO> 修饰数据ing...")
        for data in data_list:
            ultimate_data = data_tread.treat_two(data)  # 处理完成
            no_saved_data.append(ultimate_data)

        """存储数据"""
        full_file_name = "{}_{}".format(filename, page)
        save = SaveData(no_saved_data, full_file_name)
        save.save_in_file()


if __name__ == '__main__':
    xh_spider()
