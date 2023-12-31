#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""HTTP请求"""


"""HTTP请求的流程：
步骤1：浏览器首先向服务器发送HTTP请求，请求包括：
    方法：GET还是POST，GET仅请求资源，POST会附带用户数据
    路径：/full/url/path
    域名：由Host头指定：Host: www.sina.com.cn
    以及其他相关的Header
    如果是POST，那么请求还包括一个Body，包含用户数据
步骤2：服务器向浏览器返回HTTP响应，响应包括：
    响应代码：
        200表示成功
        3xx表示重定向
        4xx表示客户端发送的请求有错误
        5xx表示服务器端处理时发生了错误
    响应类型：由Content-Type指定
    以及其他相关的Header
    通常服务器的HTTP响应会携带内容，也就是有一个Body，包含响应的内容
    网页的HTML源码就在Body中
步骤3：如果浏览器还需要继续向服务器请求其他资源，比如图片
就再次发出HTTP请求，重复步骤1、2

Web采用的HTTP协议采用了非常简单的请求-响应模式，从而大大简化了开发
当编写一个页面时，只需要在HTTP请求中把HTML发送出去
不需要考虑如何附带图片、视频等
浏览器如果需要请求图片和视频，它会发送另一个HTTP请求
因此，一个HTTP请求只处理一个资源

HTTP协议同时具备极强的扩展性，虽然浏览器请求的是http://www.sina.com.cn/的首页
但是新浪在HTML中可以链入其他服务器的资源
比如<img src="http://i1.sinaimg.cn/home/2013/1008/U8455P30DT20131008135420.png">
从而将请求压力分散到各个服务器上，并且，一个站点可以链接到其他站点
无数个站点互相链接起来，就形成了World Wide Web，简称WWW
"""