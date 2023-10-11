#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from lxml import etree


"""1. 获取所有<li>标签"""
html = etree.parse("./hello.html")
print(type(html))

result_1 = html.xpath("//li")
print("<li>标签的元素集合：{}".format(result_1))  # 打印<li>标签的元素集合
print("result_1的元素数：{}".format(len(result_1)))
print("result_1的类型：{}".format(type(result_1)))
print("result_1的元素的类型：{}".format(type(result_1[0])))


"""2. 继续获取<li>标签的所有class属性"""
result_2 = html.xpath("//li/@class")
print("<li>标签的所有class属性：{}".format(result_2))


"""3. 继续获取<li>标签下 href 为 link1.html 的 <a> 标签"""
result_3 = html.xpath("//li/a[@href='link1.html']")
print("<li>标签下 href 为 link1.html 的 <a> 标签：{}".format(result_3))


"""4. 获取<li> 标签下的所有 <span> 标签"""
result_4 = html.xpath("//li//span")
print("<li> 标签下的所有 <span> 标签：{}".format(result_4))


"""5. 获取 <li> 标签下的<a>标签里的所有 class"""
result_5 = html.xpath("//li/a//@class")
print("<li> 标签下的<a>标签里的所有 class：{}".format(result_5))


"""6. 获取最后一个 <li> 的 <a> 的 href"""
result_6 = html.xpath("//li[last()]/a/@href")   # 谓语[last()]
print("最后一个 <li> 的 <a> 的 href：{}".format(result_6))


"""7. 获取倒数第二个元素的内容"""
result_7 = html.xpath("//li[last()-1]/a")
print("倒数第二个元素的内容：{}".format(result_7))


"""8. 获取 class 值为 bold 的标签名"""
result_8 = html.xpath("//*[@class='bold']")
print("class 值为 bold 的标签名：{}".format(result_8[0].tag))  # tag方法获取标签名
