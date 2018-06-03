# -*- coding: utf-8 -*-
import scrapy
import items

class PornhubUserSpider(scrapy.Spider):
    name = "PornhubUserSpider"  # 模块name
    allowd_domain = ["pornhub.com"]     # 模块的工作域
    start_urls = ["https://www.pornhub.com/users/lolitasstar/videos/public"]

    def parse(self,response):
        #video_boxs = response.xpath("//div[@class = 'profileContentLeft float-left']/section/div/div[@class = 'profileVids']/div[@class = 'videoUList/ul/li']").extract()
        results = response.xpath("//ul[@class = 'videos row-3-thumbs']/li[@class = 'js-pop videoblock videoBox']/div/div[@class = 'phimage']/div[@class = 'img fade fadeUp videoPreviewBg']/a/@href").extract()
        nums = len(results)
        for result in results:
            url = "https://www.pornhub.com" + result
            yield scrapy.Request(url=url, callback=self.parse_unit)
        next_page_key = response.xpath("//button[@id = 'moreDataBtn']").extract()
        if len(next_page_key) > 0:
            yield scrapy.FormRequest(url = "https://www.pornhub.com/users/lolitasstar/videos/public?page=2",callback = self.parse)

    '''
    def parse_another(self,response):
        results = response.xpath("//ul[@class = 'videos row-3-thumbs']/li[@class = 'js-pop videoblock videoBox']/div/div[@class = 'phimage']/div[@class = 'img fade fadeUp videoPreviewBg']/a/@href").extract()
        nums = len(results)
        pass
    '''

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
        item = items.UltispiderItem(Url = url,Title = title,Views = views,Uploader = uploader,Categories = categories,Favorable_rating = favorable_rating,Is_check = False)
        yield item