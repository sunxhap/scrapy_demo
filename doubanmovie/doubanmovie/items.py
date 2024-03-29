# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class DoubanmovieItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass

    name = scrapy.Field()  # 电影名称
    url = scrapy.Field()  # 电影详情主页
    rating = scrapy.Field()  # 电影评分