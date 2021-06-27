import scrapy
from scrapy.crawler import CrawlerProcess

class deadlinespider(scrapy.Spider):
    name = 'deadline'
    start_urls = ['https://www.deadlinenews.co.uk/category/news/']

    def parse(self, response):
        for article in  response.css('div.td-ss-main-content').css('h3.entry-title.td-module-title'):
            yield {
                'link': article.css('a').attrib['href'],
                'title': article.css('a::text').get(),
                'is_sarcsam': 0
            }
        date = int(response.css('div.td-ss-main-content').css('time.entry-date.updated.td-module-date::text')[-1].get().split()[-1])
        next_page = response.css('div.page-nav.td-pb-padding-side').css('a')[-1].attrib['href']   
        if next_page is not None and date >= 2018:
            yield response.follow(next_page, callback=self.parse)

process = CrawlerProcess(settings={
    "FEEDS": {
        "is_sarcastic_v2.json": {"format": "json", 'encoding': 'utf8'},
    },
})

process.crawl(deadlinespider)
process.start()