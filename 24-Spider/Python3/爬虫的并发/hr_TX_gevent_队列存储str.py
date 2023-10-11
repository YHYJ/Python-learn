# -*- coding: utf-8 -*-

"""协程 gevent"""

import random
import gevent
import requests

from queue import Queue
from gevent import monkey
from bs4 import BeautifulSoup

from conf.User_Agent_list import USER_AGENT_LIST


monkey.patch_all()


class TXSpider:
    """腾讯社招前3页"""
    def __init__(self):
        _basic_url = "http://hr.tencent.com/position.php?&start="
        self.start_urls = ["{}{}".format(_basic_url, str(num))
                           for num in range(0, 21, 10)]
        self.headers = {"User-Agent": random.choice(USER_AGENT_LIST)}
        self.data_queue = Queue()
        self.data_queue.put("{}\t{}\t{}\t{}\t{}\t{}".format(
            "职位名", "链接", "职位类别", "招聘人数", "工作地点", "发布时间")
        )

    def send_request(self, url):
        """发送请求，接收响应"""
        try:
            html_data = requests.get(url, headers=self.headers).content
            self.parse_data(html_data)
        except Exception as e:
            print("<ERROR_INFO>：数据抓取失败!--->{}\n<---".format(e))
            return None

    def parse_data(self, html_data):
        """处理数据"""
        soup = BeautifulSoup(html_data, "lxml")
        node_list = soup.find_all("tr", {"class": ["even", "odd"]})

        for node in node_list:
            '''职位名、详情链接、职位类别、招聘人数、工作地点、发布时间'''
            position_name = node.find("a").get_text()
            position_link = "{}{}".format(
                "http://hr.tencent.com/", node.find("a").get("href")
            )
            position_type = node.find_all("td")[1].get_text()
            position_num = node.find_all("td")[2].get_text()
            position_site = node.find_all("td")[3].get_text()
            position_time = node.find_all("td")[4].get_text()

            self.data_queue.put("{}\t{}\t{}\t{}\t{}\t{}".format(
                position_name, position_link, position_type,
                position_num, position_site, position_time))

    def start_work(self):
        """任务调度"""
        print("<INIT_INFO>：初始化任务，请稍候...")

        job_list = [gevent.spawn(self.send_request, url)
                    for url in self.start_urls]

        gevent.joinall(job_list)

        while not self.data_queue.empty():
            print(self.data_queue.get())

        print("Finished O(∩_∩)0~~~")


if __name__ == "__main__":
    tx = TXSpider()
    tx.start_work()
