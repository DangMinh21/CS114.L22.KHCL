import scrapy
from scrapy.crawler import CrawlerProcess

class beavertonspider(scrapy.Spider):
    name = 'beaverton'
    start_urls = ['https://www.thebeaverton.com/']

    def parse(self, response):
        for article in  response.css('div.posts.border.ajaxify-pagination').css('header.post-title.entry-header'):
            yield {
                'article_link': article.css('a').attrib['href'],
                'headline': article.css('a::text').get(),
                'is_sarcastic': 1
            }
        date = int(response.css('time.time')[-1].attrib['datetime'].split('-')[0])
        next_page =response.css('a.next.page-numbers').attrib['href']   
        if next_page is not None and date >= 2018:
            yield response.follow(next_page, callback=self.parse)

process = CrawlerProcess(settings={
    "FEEDS": {
        "beaverton.json": {"format": "json", 'encoding': 'utf8'},
    },
})

process.crawl(beavertonspider)
process.start()