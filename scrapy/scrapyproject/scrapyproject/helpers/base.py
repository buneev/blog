from scrapy import Spider
from scrapy import signals
from copy import deepcopy
from datetime import datetime
import requests
import json

BLOG_URL = 'http://127.0.0.1:8000'


class BaseSpider(Spider):

    @classmethod
    def from_crawler(cls, crawler):
        
        # instantiate the extension object
        ext = cls(crawler.spidercls.name)
        # ext = cls(dest_url, crawler.spidercls.name)

        # connect the extension object to signals
        crawler.signals.connect(ext.spider_opened, signal=signals.spider_opened)
        crawler.signals.connect(ext.spider_closed, signal=signals.spider_closed)
        crawler.signals.connect(ext.item_scraped, signal=signals.item_scraped)
        
        # return the extension object
        return ext

    def spider_opened(self, spider):
        self._part = 0
        self._articles = list()
        self.start_time=datetime.utcnow()
        self.dest_url = f'{BLOG_URL}/article/api/'
        self.count = 500 # max cnt artile for send to django
        spider.logger.info("Spider opened: %s", spider.name)

    def spider_closed(self, spider):
        spider.logger.info('Spider closed: %s', spider.name)
        if len(self._articles) > 0:
            self._send_file(self._articles, spider)

    def item_scraped(self, item, spider):
        self._articles.append(deepcopy(item))
        if len(self._articles) >= self.count:
            self._send_file(self._articles, spider)

    def _send_file(self, articles=None, spider=None):
        spider.logger.info(f"Spider '{spider.name}' ends work, request to: {self.dest_url}")
        try:
            file = json.dumps(articles)
            # files = {'job_file (str(self._part), file)}
            data = {'spider': spider.name}
            data.update({'start_time': self.start_time,
                         'finish_time': datetime.utcnow(),
                         'item_scraped_count': len(articles)})
            r = requests.post(url=self.dest_url, data=file)
            if r.status_code == 200:
                spider.logger.info("Data sent successful")
                self._items = list()
                self._part = self._part + 1
            else:
                spider.logger("Bad response: status_code={}".format(r.status_code))
        except json.JSONDecodeError:
            spider.logger("Error encode items to json")


    def get_art_container(self):
        result = {
            "site": "ria.ru",
            "url": "",
            "code": "",
            "title": "",
            "text": "",
            "images": [],
            "date": "",
            "author": [],
        }
        return result
