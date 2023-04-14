import scrapy
import pandas as pd
from bs4 import BeautifulSoup


class BusinessTodaySpider(scrapy.Spider):
    name = 'business_today'
    allowed_domains = ['esg.businesstoday.com.tw']
    start_urls = ['http://esg.businesstoday.com.tw/catalog/180686/']

    def __init__(self, dataset='Train'):
        # args: dataset = 'Train' or 'Dev'
        self.data = pd.read_json(f'./data/ML-ESG_Chinese_{dataset}.json')

    def parse(self, response):
        urls = self.data.URL.to_list()

        for url in urls:
            yield scrapy.Request(url, self.parse_content, dont_filter=True)


    def parse_content(self, response):
        news_url = response.request.url
        news_content_html = response.xpath("//div[@class='cke_editable font__select-content']/div").getall()
        news_content = self.clean_data(news_content_html[0])

        idx = self.data[self.data.URL == news_url].index[0]

        EsgCrawlerItem = {
            'news_pk': int(self.data.news_pk[idx]),
            'URL': news_url,
            'news_title': str(self.data.news_title[idx]),
            'ESG_label': list(self.data.ESG_label[idx]),
            'news_content_html': news_content_html,
            'news_content': news_content
        }

        yield EsgCrawlerItem


    def clean_data(self, content_html):
        soup = BeautifulSoup(content_html, 'html.parser')
        content = soup.get_text()

        content = content.replace('\n', ' ')
        content = content.replace('\r', '')
        content = content.replace('\xa0', '')

        idx_1 = content.find('※本文')
        idx_2 = content.find('延伸閱讀')

        if (idx_1 > 5) | (idx_2 > 5):
            content = content[:min(idx_1, idx_2)]

        return content