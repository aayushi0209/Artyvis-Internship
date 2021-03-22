import scrapy
from scrapy.selector import Selector

from scrapy.item import Item, Field


class StackItem(Item):
    image = Field()
    name = Field()
    price = Field()


class DataSpider(scrapy.Spider):
    name = "data"

    def start_requests(self):
        urls = [
            "https://www.houseofindya.com/zyra/necklace-sets/cat",
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
       
        data_get=Selector(response).xpath(('//*[@id="JsonProductList"]/li'))

        for i,d in enumerate(data_get):   
            data = StackItem()
            data['image'] = d.xpath('//*[@id="JsonProductList"]/li[{}]/a/div[1]/img/@data-original'.format(i+1)).extract()[0]
            data['name'] = d.xpath('//*[@id="JsonProductList"]/li[{}]/a/div[2]/p/text()'.format(i+1)).extract()[0]
            data['price']=d.xpath('//*[@id="JsonProductList"]/li[{}]/a/div[3]/span[1]/text()'.format(i+1)).extract()[0]
            yield data

   