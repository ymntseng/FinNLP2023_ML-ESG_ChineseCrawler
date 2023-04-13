import scrapy
import pandas as pd

class BusinessTodaySpider(scrapy.Spider):
    name = 'business_today'
    allowed_domains = ['esg.businesstoday.com.tw']
    start_urls = ['http://esg.businesstoday.com.tw/catalog/180686/']


    def parse(self, response):
        urls = pd.read_csv('./esg_crawler/dev_url.csv').URL.to_list()

        for url in urls:
            yield scrapy.Request(url, self.parse_content, dont_filter=True)


    def parse_content(self, response):
        news_url = response.request.url
        news_content_html = response.xpath("//div[@class='cke_editable font__select-content']/div").getall()

        EsgCrawlerItem = {
            'news_url': news_url,
            'news_content_html': news_content_html
        }

        yield EsgCrawlerItem