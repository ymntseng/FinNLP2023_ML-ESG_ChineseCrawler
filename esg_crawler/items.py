# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class EsgCrawlerItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()

    # origin
    news_pk = scrapy.Field()
    URL = scrapy.Field()
    news_title = scrapy.Field()
    ESG_label = scrapy.Field()

    # new add by crawler
    news_content_html = scrapy.Field()
    news_content = scrapy.Field()