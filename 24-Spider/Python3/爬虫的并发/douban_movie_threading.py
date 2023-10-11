# -*- coding: utf-8 -*-

"""多线程 threading"""

import random
import requests
import threading


from queue import Queue
from bs4 import BeautifulSoup

from conf.User_Agent_list import USER_AGENT_LIST


class Douban:
    """
    抓取豆瓣电影TOP250
    https://movie.douban.com/top250?start=0
    https://movie.douban.com/top250?start=25
    https://movie.douban.com/top250?start=50
    ...
    https://movie.douban.com/top250?start=225
    """
    def __init__(self):
        _basic_url = "https://movie.douban.com/top250?start="
        self.headers = {"User-Agent": random.choice(USER_AGENT_LIST)}
        self.start_urls = ["{}{}".format(_basic_url, str(num))
                           for num in range(0, 226, 25)]
        self.data_queue = Queue()

    def send_request(self, url):
        """发送请求"""
        print("<INFO>：正在处理{}".format(url))
        response = requests.get(url, headers=self.headers)
        self.parse_data(response)

    def parse_data(self, html_data):
        """处理数据"""
        soup = BeautifulSoup(html_data.content, "lxml")
        node_list = soup.find_all("div", {"class": "info"})

        for node in node_list:
            """电影标题、评分"""
            title = node.find("span").get_text()
            score = node.find("span", {"class": "rating_num"}).get_text()
            # print("评分：{}，{}".format(score, title))
            self.data_queue.put("{}\t{}".format(score, title))

    def start_work(self):
        """任务调度"""
        thread_list = []
        for url in self.start_urls:
            thread = threading.Thread(target=self.send_request, args=[url])
            thread.start()
            thread_list.append(thread)

        for thread in thread_list:
            thread.join()

        while not self.data_queue.empty():
            print(self.data_queue.get())


if __name__ == "__main__":
    douban = Douban()
    douban.start_work()
