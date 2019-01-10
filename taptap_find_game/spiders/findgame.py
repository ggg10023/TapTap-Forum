# -*- coding: utf-8 -*-
import scrapy
from taptap_find_game.items import TaptapFindGameItem


class FindgameSpider(scrapy.Spider):
    name = 'findgame'
    allowed_domains = ['www.tatap.com']
    start_urls = ['https://www.taptap.com/topic/4113542?order=desc'] #起始链接，在官方网址https://www.taptap.com/forum/g26中找到最新的一条链接，作为起始链接。

    #def start_requests(self):
       # base_url ='https://www.taptap.com/forum/g26?type=all&sort=created&page={}'
       # for id in range(1,500):
       #     full_url =base_url.format(str(id))
       #     yield scrapy.Request(url=full_url,callback=self.parse_list)
      #  base_url = 'https://www.taptap.com/topic/3652534'

#    def parse_list(self,response):
#        topic_list = response.xpath("//a[@class='item-text-title']/@href").extract()
#        for topic in topic_list:
#            url = str(topic)
#            yield scrapy.Request(url=url,callback=self.parse)

    def parse(self, response):
        item = TaptapFindGameItem()
        item['main_topic'] = response.xpath('//h1/text()').extract_first().replace(" ","").strip()
        item['author'] = response.xpath("//div[@class='first-header-topic']/span/a[@class='taptap-user-name taptap-link']/text()").extract_first()
        item['author_id'] = response.xpath("//div[@class='first-header-topic']/span/a[@class='taptap-user-name taptap-link']/@href").extract_first().split('/')[-1]
        item['topic_details'] = response.xpath("//div[@class='main-first-body bbcode-body js-open-bbcode-image']/text()").extract_first().strip()
        item['topic_replies'] = response.xpath("//button[@class='btn btn-lg taptap-button-opinion comment']/span/text()").extract_first()
        item['topic_id'] = response.url.split('/')[-1].replace('?order=desc','')
        item['topic_time'] = response.xpath("//span[@class='first-header-time']/text()").extract_first()
        item['topic_view'] = response.xpath("//span[@class='topic-hit']/span/text()").extract_first()
        item['topic_final_reply'] = response.xpath("//div[@class='show-main-posts']/div[1]/div/div/a[2]/span/text()").extract_first()
        #print(item['main_topic'])
        yield item
        next_url = response.xpath("//div[@class='main-next-prev-common'][2]/a/@href").extract_first()
        next_url = next_url+'?order=desc'
        if next_url is not None:
            yield scrapy.Request(url=next_url,callback=self.parse,dont_filter=True)
