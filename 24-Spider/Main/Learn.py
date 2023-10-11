#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import urllib.parse
import urllib.request


data = {}
# data["word"] = "Jecvay Notes"

url = "https://www.baidu.com/"
# url_values = urllib.parse.urlencode(data)
full_url = url

data = urllib.request.urlopen(full_url).read()
data = data.decode("UTF-8")
# headers = {"User-Agent": "Baiduspider+"}


if __name__ == '__main__':
    print(type(data), data)  # 爬得的数据是字符串
    with open("data/Learn.html", "w") as f:
        f.write(data)
