# -*- coding: utf-8 -*-
import scrapy
import items




class PornhubSpider(scrapy.Spider):
    name = "PornhubSpider"  # 模块name
    allowd_domain = ["pornhub.com"]     # 模块的工作域
    start_urls = ["https://www.pornhub.com/video?c=15&o=mv&t=a"]
    #start_urls = ["https://www.pornhub.com/view_video.php?viewkey=ph58a25a3f48b1e"]

    '''
        用于具体的response解析
        @:param
            response: 网页的响应
    '''

    def parse(self,response):
        results = response.xpath("//ul[@class = 'nf-videos videos search-video-thumbs']//div[@class = 'wrap']/div[@class = 'thumbnail-info-wrapper clearfix']/span[@class = 'title']/a/@href").extract()
        for result in results:
            url = u"https://www.pornhub.com" + result  # target url
            yield scrapy.Request(url = url,callback = self.parse_unit)
        next_page_key =  response.xpath("//li[@class = 'page_next']/a/@href").extract()
        if len(next_page_key) > 0:
            next_page_url =  u"https://www.pornhub.com" + next_page_key[0]
            yield scrapy.Request(url = next_page_url,callback = self.parse)

    def parse_unit(self, response):
        '''
        this func used to pase video web
        :param response: http response after downloader download the html
        :return:    UltispiderItem
        '''

        #quality
            # TODO: 可以通过对url来提取得到当前url所对应的清晰度
        url = response.url
        title = views = uploader = categories = favorable_rating = []
        # title {list}
        results = response.xpath("//span[@class = 'inlineFree']/text()").extract()
        if len(results) != 0:
            title = results[0]
        # views {list}
        results = response.xpath("//span[@class = 'count']/text()").extract()
        if len(results) != 0:
            views = results[0]
        # uploader {list}
        results = response.xpath("//div[@class = 'usernameWrap clearfix' and @data-type = 'user']/a/text()").extract();
        if len(results) != 0:
            uploader = results[0]
        # categories {list}
        results = response.xpath("//div[@class = 'categoriesWrapper']/a/text()").extract()
        if len(results) != 0:
            categories = results[0]
        # favorable rating {list}
        results = response.xpath("//span[@class = 'percent']/text()").extract()
        if len(results) != 0:
            favorable_rating = results[0]
        #item = items.UltispiderItem(file_url = url,Title = title,Views = views, Uploader = uploader, Categories = categories, Favorable_rating = favorateble_rating)
        item = items.UltispiderItem(Url = url,Title = title,Views = views,Uploader = uploader,Categories = categories,Favorable_rating = favorable_rating)
        yield item


