# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class UltispiderItem(scrapy.Item):
    # define the fields for your item here like:
    Url = scrapy.Field()  # URL
    Title = scrapy.Field()  # 标题
    #Quality = scrapy.Field()  # 清晰度

    Views = scrapy.Field() # 浏览次数
    Uploader = scrapy.Field() # 上传者
    Categories = scrapy.Field() # 标签
    Favorable_rating = scrapy.Field() # 好评率
    Is_check = scrapy.Field() # 是否已经下载

    pass
