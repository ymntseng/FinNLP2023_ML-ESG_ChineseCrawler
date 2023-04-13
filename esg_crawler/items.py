# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class EsgCrawlerItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()

    news_url = scrapy.Field()
    news_content_html = scrapy.Field()
