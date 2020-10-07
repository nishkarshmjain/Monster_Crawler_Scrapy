import scrapy


class MonsterSpider(scrapy.Spider):
    name = 'MonsterSpider'
    allowed_domains = ['monster.com']
    start_urls = ['http://monster.com/']

    def parse(self, response):
        pass
