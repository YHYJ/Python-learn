## spider里parse()的机制

```python
def parse(self, response):
    """处理招聘信息列表页
        :yield: url: 深入处理的URL
        :yield: meta: 回调函数的参数
        :yield: callback: 回调函数，调用self.parse_page
        """
    node_list = response.xpath("//tr[@class='even'] | //tr[@class='odd']")

    for node in node_list:
        item = HrTxItem()

        item["post_name"] = node.xpath(".//a/text()").extract_first()
        item["post_link"] = "http://hr.tencent.com/{}".format(
            node.xpath(".//a/@href").extract_first()
        )
        item["post_type"] = node.xpath("./td[2]/text()").extract_first()
        item["post_nums"] = node.xpath("./td[3]/text()").extract_first()
        item["post_site"] = node.xpath("./td[4]/text()").extract_first()
        item["post_time"] = node.xpath("./td[5]/text()").extract_first()

        yield item																# ①
        yield scrapy.Request(url=item["post_link"], callback=self.parse_page)	# ②
```



1. ①使用yield返回解析结果，所以parse()是一个生成器函数，scrapy引擎逐个获取parse()方法中生成的结果并判断其类型

   > 如果是request则加入抓取队列，如果是item则交给pipeline进行处理
   >
   > 其他类型，返回错误信息

2. scrapy引擎取到第一批request（从start_urls）后存入到队列

3. 第一批request获取完成，发送并获取response，将response放到parse()进行解析，得到结果item

4. 判断item的类型，将request由scrapy引擎交给队列进行去重入队，item则交给pipeline处理

5. 新的response经由callback回调函数交给下一个parse()解析后得到item，循环4、5直到队列为空

* 程序在取得各个页面的items前，会先处理完队列里所有的request请求，然后提取items
* 所有操作有scrapy引擎和调度器负责

