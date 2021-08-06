import scrapy
from scrapy.crawler import CrawlerProcess

class crikeyspider(scrapy.Spider):
    name = 'crikey'
    start_urls = ['https://www.crikey.com.au/politics/',
                  'https://www.crikey.com.au/business/',
                  'https://www.crikey.com.au/media/',
                  'https://www.crikey.com.au/state-politics/',
                  'https://www.crikey.com.au/life/',
                  'https://www.crikey.com.au/world/']

    def parse(self, response):
        for article in response.css('div.details'):
            yield {
                'link': article.css('a').attrib['href'],
                'title': article.css('h2::text').get(),
                'is_sarcsam': 0
            }
        date = int(response.css('div.details').css('p.date::text').get().split()[-1])
        next_page =  response.css('a.next.page-numbers').attrib['href']   
        if next_page is not None and date >= 2018:
            yield response.follow(next_page, callback=self.parse)

process = CrawlerProcess(settings={
    "FEEDS": {
        "is_sarcastic_v2.json": {"format": "json", 'encoding': 'utf8'},
    },
})

process.crawl(crikeyspider)
process.start()