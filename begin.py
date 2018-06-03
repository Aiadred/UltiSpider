# -*- coding: utf-8 -*-

from scrapy import  cmdline
#from scrapy.crawler import  CrawlerProcess
#from scrapy.utils.project import get_project_settings
'''
# get_project_settings 为获取settings中的设置信息
process = CrawlerProcess(get_project_settings())
# param为要启动的爬虫
process.crawl('PornhubSpider')
process.start()
'''

# 另一种启动爬虫的方法
cmdline.execute("scrapy crawl PornhubUserSpider".split())