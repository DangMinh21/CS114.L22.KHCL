import scrapy
from scrapy.crawler import CrawlerProcess

class thepokespider(scrapy.Spider):
    name = 'thepoke'
    start_urls = ['https://www.thepoke.co.uk/category/news/']

    def parse(self, response):
        for article in  response.css('article.boxgrid > a'):
            yield {
                'link': article.attrib['href'],
                'title': article.css('p::text').get(),
                'is_sarcsam': 1
            }

        next_page = response.css('div.prev > a').attrib['href']    
        if next_page is not None:
            yield response.follow(next_page, callback=self.parse)

process = CrawlerProcess(settings={
    "FEEDS": {
        "items.json": {"format": "json"},
    },
})

process.crawl(thepokespider)
process.start()