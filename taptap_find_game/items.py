# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class TaptapFindGameItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    # define the fields for your item here like:
    main_topic = scrapy.Field()
    author = scrapy.Field()
    author_id = scrapy.Field()
    #publish_time = scrapy.Field()
    topic_details = scrapy.Field()
    topic_replies = scrapy.Field()
    topic_time = scrapy.Field()
    topic_id = scrapy.Field()
    topic_view = scrapy.Field()
    topic_final_reply = scrapy.Field()