# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymongo
from scrapy.exceptions import DropItem

class PornhubSpiderPipeline(object):
    def __init__(self,mongo_uri,mongo_db):

        self.mongo_db = mongo_db
        self.mongo_uri = mongo_uri


    def process_item(self,item,spider):
        if len(item['Title']) == 0:
            DropItem(item)
        else:
            #line = json.dumps(dict(item)) + "\r\n"
            #self.fd.write(line)
            # write to mongodb
            collections = self.db['hubItem']
            collections.insert(dict(item))

    '''
    import mongdb's config
    '''
    @classmethod
    def from_crawler(cls,crawler):
        return cls(mongo_uri = crawler.settings.get('MONGO_URI'),mongo_db = crawler.settings.get('MONGO_DB'))


    def close_spider(self,spider):
        #self.fd.close()
        self.client.close()


    def open_spider(self,spider):
        #self.fd = codecs.open("./FileStore/data.json", "wb", encoding='utf-8')
        self.client = pymongo.MongoClient(self.mongo_uri)
        self.db = self.client[self.mongo_db]






