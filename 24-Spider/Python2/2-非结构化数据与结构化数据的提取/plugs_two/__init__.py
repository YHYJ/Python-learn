# -*- coding: utf-8 -*-


def xiaohua_info():
    """
    打印提示信息
    :return: de_code    网页原始编码
             en_code    转码格式，默认utf-8
             a_page     起始抓取页码
             e_page     结束抓取页码
             filename   存储数据的文件名
             file_type  文件后缀名，默认无
             file_dir   存储路径，默认 './data/html/'
    """
    de_code = raw_input("网页原始编码(utf-8)：")
    en_code = raw_input("期望编码(utf-8)：")
    a_page = int(raw_input("起始页码："))
    e_page = int(raw_input("结束页码："))
    filename = raw_input("文件名：")
    # file_type = raw_input("文件类型(None)：")
    s_dir = raw_input("存储路径(<html> or <image>)：")
    file_dir = "{}{}{}".format("./data/", s_dir, "/")
    param = {
        "de_code": de_code,
        "en_code": en_code,
        "a_page": a_page,
        "e_page": e_page,
        "filename": filename,
        # "file_type": file_type,
        "file_dir": file_dir,
    }
    return param


def tieba_info():
    """
    打印提示信息
    :return: de_code    网页原始编码
             en_code    转码格式，默认utf-8
             a_page     起始抓取页码
             e_page     结束抓取页码
             filename   存储数据的文件名
             file_type  文件后缀名，默认无
             file_dir   存储路径，默认 './data/html/'
    """
    a_page = int(raw_input("起始页码："))
    e_page = int(raw_input("结束页码："))
    s_dir = raw_input("存储路径(<html> or <image>)：")
    file_dir = "{}{}{}".format("./data/", s_dir, "/")
    param = {
        "a_page": a_page,
        "e_page": e_page,
        "file_dir": file_dir,
    }
    return param
