#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import json
import random
import requests

from bs4 import BeautifulSoup

from conf.User_Agent_list import USER_AGENT_LIST


class TXSpider:
    def __init__(self, page=None, value="y"):
        self.basic_url = "http://hr.tencent.com/position.php?&start=0"
        self.headers = {"User-Agent": random.choice(USER_AGENT_LIST)}
        self.item_list = []
        self.value = value
        self.page = int(page)

    def send_request(self, url):
        """
        发送请求，接收响应
        """
        try:
            html_data = requests.get(url, headers=self.headers).content
            return html_data
        except Exception as e:
            print("<ERROR_INFO>：数据抓取失败!\n--->{}".format(e))
            return None

    def parse_data(self, html_data):
        """
        处理数据
        """
        # 使用bs4调用 lxml 解析器解析响应数据
        soup = BeautifulSoup(html_data, "lxml")
        # 查找带有招聘信息的标签
        node_list = soup.find_all("tr", {"class": ["even", "odd"]})

        # 处理数据
        for node in node_list:
            item = {}
            '''职位名、详情链接、职位类别、招聘人数、工作地点、发布时间'''
            item["position_name"] = node.find("a").get_text()
            item["position_link"] = "{}{}".format("http://hr.tencent.com/", node.find("a").get("href"))
            item["position_type"] = node.find_all("td")[1].get_text()   # index = 1：职位类别
            item["position_num"] = node.find_all("td")[2].get_text()    # index = 2：招聘人数
            item["position_site"] = node.find_all("td")[3].get_text()   # index = 3：工作地点
            item["position_time"] = node.find_all("td")[4].get_text()   # index = 4：发布时间

            self.item_list.append(item)

        # 判断当前是否最后一页
        if soup.find("a", {"id": "next", "class": "noactive"}):
            return True
        else:
            next_page_link = "{}{}".format("http://hr.tencent.com/", soup.find("a", {"id": "next"}).get("href"))
            return next_page_link

    def save_data(self, page_num="0"):
        """
        将处理后的数据转换成JSON格式并存储
        根据self.value的值判断是否分页存储，分页则根据page_num值区分文件名
        """
        if self.value == "y":
            file_name = "./data/JSON/hr_TX_bs4_P{}.json".format(page_num)
        else:
            file_name = "./data/JSON/hr_TX_bs4.json"

        print("<SAVE_INFO>：正在存储数据...")
        json.dump(self.item_list, open(file_name, "w"))

    def multifile_save(self):
        """
        任务调度，多文件存储
        """
        print("<INIT_INFO>：初始化任务，请稍候...")

        html_data = self.send_request(self.basic_url)

        for page_num in range(1, self.page + 1):
            print("<SPIDER_INFO>：正在抓取第{}页".format(page_num))
            next_page_link = self.parse_data(html_data)

            if next_page_link is True:
                '''如果到了最后一页'''
                break
            else:
                '''根据返回的链接请求下一页'''
                html_data = self.send_request(next_page_link)

            self.save_data(page_num=str(page_num))
            self.item_list = []  # 存完一页，清空招聘信息列表

        print("Finished O(∩_∩)0~~~")

    def monofile_save(self):
        """
        任务调度，单文件存储
        """
        print("<INIT_INFO>：初始化任务，请稍候...")

        html_data = self.send_request(self.basic_url)

        for page_num in range(1, self.page + 1):
            print("<SPIDER_INFO>：正在抓取第{}页".format(page_num))
            next_page_link = self.parse_data(html_data)

            if next_page_link is True:
                '''如果到了最后一页'''
                break
            else:
                '''根据返回的链接请求下一页'''
                html_data = self.send_request(next_page_link)

        self.save_data()
        print("Finished O(∩_∩)0~~~")


if __name__ == "__main__":
    page = raw_input("抓取页数：")
    value = raw_input("是否分页(y/n)：")

    spider = TXSpider(page, value)

    if value is "y":
        spider.multifile_save()
    elif value is "n":
        spider.monofile_save()
    else:
        print("<ERROR_INFO>：参数错误!")
