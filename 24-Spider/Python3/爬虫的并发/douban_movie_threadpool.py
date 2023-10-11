# -*- coding: utf-8 -*-

"""多线程 threadpool线程池"""

import random
import requests
import threadpool as Pool

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
        """
        URL、headers、数据队列
        """
        _basic_url = "https://movie.douban.com/top250?start="
        self.start_urls = ["{}{}".format(_basic_url, str(num))
                           for num in range(0, 226, 25)]
        self.headers = {"User-Agent": random.choice(USER_AGENT_LIST)}
        self.data_queue = Queue()

    def send_request(self, url):
        """发送请求"""
        print("<INFO>：正在处理{}".format(url))
        response = requests.get(url, headers=self.headers)
        return response

    def parse_data(self, html_data):
        """处理数据"""
        soup = BeautifulSoup(html_data, "lxml")
        node_list = soup.find_all("div", {"class": "info"})

        for node in node_list:
            """电影标题、评分"""
            title = node.find("span").get_text()
            score = node.find("span", {"class": "rating_num"}).get_text()
            self.data_queue.put("{}\t{}".format(title, score))

    def start_work(self):
        """任务调度"""
        pool = Pool.ThreadPool(len(self.start_urls))
        reques = Pool.makeRequests(self.send_request,
                                   args_list=self.start_urls)
        [pool.putRequest(i) for i in reques]
        pool.wait()


if __name__ == "__main__":
    douban = Douban()
    douban.start_work()
