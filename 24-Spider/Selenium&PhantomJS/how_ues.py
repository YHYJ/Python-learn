# -*- coding: utf-8 -*-

"""
Date: 2018-01-02 21:01:55
Last modified: 2018-01-02 21:01:55
Author: YJ1516 - yj1516268@outlook.com

"""

from selenium import webdriver


driver = webdriver.PhantomJS()      # 调用PhantomJS浏览器创建浏览器对象

driver.get("http://www.baidu.com/")
"""get方法等到页面完全加载才会继续执行"""

data = driver.find_element_by_id("wrapper").text
print("获取id='wrapper'的标签的内容：\n{}".format(data))

print("\n当前页面标题：{}".format(driver.title))

driver.save_screenshot("baidu.png")  # 生成当前页面截图并保存


"""模拟搜索过程"""
# id = 'kw'是百度搜索栏id
driver.find_element_by_id("kw").send_keys(u"bing")
# id = 'su'是搜索按钮id

driver.find_element_by_id("su").click()     # 模拟点击动作
driver.save_screenshot("search_bing.png")

# print(driver.page_source)
