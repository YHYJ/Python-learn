#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import urllib.request
import json
from city import city

while 1:
    cityname = input('你想查询哪个城市的天气状况?\n')
    citycode = city.get(cityname)
    if citycode:    #防止输入列表中没有的城市，用if判断citycode是否存在
        try:
            url = ('http://www.weather.com.cn/data/cityinfo/%s.html' % citycode)
            content = urllib.request.urlopen(url).read()
            #print(content)      #输出json格式的天气信息，接下来处理信息
            #print(content.decode('utf-8'))
            content1 = content.decode('utf-8')  #用 decode() 方法将从网络或者存储设备读取的bytes类型的字节流转为str类型
            data = json.loads(content1)
            jieguo = data['weatherinfo']
            str_temp = ('%s\n%s ~ %s') % (
                jieguo['weather'],
                jieguo['temp1'],
                jieguo['temp2']
            )
            print(str_temp)
        except:
            print('查询失败')
    else:
        print('没有找到该城市')