import scrapy
from scrapy.crawler import CrawlerProcess

class clickholespider(scrapy.Spider):
    name = 'clickhole'
    start_urls = ['https://clickhole.com/']

    def parse(self, response):
        for article in response.css('h2.post-title'):
            yield {
                'article_link': article.css('a').attrib['href'],
                'headline': article.css('a::text').get(),
                'is_sarcastic': 1
            }
        date = int( response.css('div.post-header').css('div.post-byline::text')[-1].get().split()[-1])
        next_page = response.css('a.next.page-numbers').attrib['href'] 
        if next_page is not None and date >= 2018:
            yield response.follow(next_page, callback=self.parse)

process = CrawlerProcess(settings={
    "FEEDS": {
        "is_sarcastic.json": {"format": "json", 'encoding': 'utf8'},
    },
})

process.crawl(clickholespider)
process.start()