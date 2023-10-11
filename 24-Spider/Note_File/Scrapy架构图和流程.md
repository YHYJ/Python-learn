## Scrapy架构图和流程

#### Scrapy架构图（绿线代表数据流向）

![Scrapy架构图](./data/image/scrapy_all.png)

* Scrapy Engine（引擎）：负责 `Sciper`、`Item Pipeline`、`Doawnloader`、`Schedular`之间的信号、数据的传递
* Scheduler（调度器）：负责接收引擎发送过来的___request___请求，并按照一定方法进行整理排列、入队，当引擎需要时交还给引擎
* Downloader（下载器）：负责下载引擎发送的所有___requests___请求，并将下载的___responses___交到引擎，由引擎交给Spider进行处理
* Spider（爬虫）：负责处理所有responses，从中分析提取数据，获取item字段需要的数据，将需要跟进的URL交给引擎，再次进入调度器
* Item Pipeline（管道）：负责处理爬虫中获取到的item，并进行后期处理（详细分析、过滤、存储等）
* Downloader Middlewares（下载中间件）：供自定义的扩展下载功能的组件
* Spider Middlewares（Spider中间件）：供自定义的扩展和操作Engine和Spider之间通信的功能组件

---

## 流程

* 新建项目(**scrapy startproject <project_name>**)：新建一个新的爬虫项目
* 明确目标(**items.py**)：明确想要抓取的目标
* 制作爬虫(**spiders/project_namespider.py**)：制作爬虫开始抓取网页数据
* 存储内容(**pipelines.py**)：设计管道存储抓取的内容

