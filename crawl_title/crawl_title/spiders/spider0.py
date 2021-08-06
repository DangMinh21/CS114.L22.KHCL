import scrapy
from scrapy.crawler import CrawlerProcess


# gôm 3 class tưng ứng với 3 trang báo 
class breitbartspider(scrapy.Spider):
    name = 'breibart'
    start_urls = ['https://www.breitbart.com/politics/',
                  'https://www.breitbart.com/world-news/',
                  'https://www.breitbart.com/economy/',
                  'https://www.breitbart.com/sports/',
                  'https://www.breitbart.com/tech/',
                  'https://www.breitbart.com/the-media/',
                  'https://www.breitbart.com/entertainment/']

    def parse(self, response):
        for article in  response.css('div.tC > h2'):
            yield {
                'link': article.css('a').attrib['href'],
                'title': article.css('a::text').get(),
                'is_sarcsam': 0
            }
        # duyệt qua các page
        # lấy năm của bài báo ở vị trí cuối page 
        date = int(response.css('div.header_byline > time').attrib['datetime'].split('-') [0])
        next_page = response.css('nav.pagination > a').attrib['href']   
        # nếu có page sau và bài báo cuối page từ năm 2018 trở đi thì tiếp tục duyêt page sau
        if next_page is not None and date >= 2018:
            yield response.follow(next_page, callback=self.parse)

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
        ## duyệt qua các page
        # lấy năm của bài báo ở vị trí cuối page 
        date = int(response.css('div.td-ss-main-content').css('time.entry-date.updated.td-module-date::text')[-1].get().split()[-1])
        next_page = response.css('div.page-nav.td-pb-padding-side').css('a')[-1].attrib['href']  
        # nếu có page sau và bài báo cuối page từ năm 2018 trở đi thì tiếp tục duyêt page sau 
        if next_page is not None and date >= 2018:
            yield response.follow(next_page, callback=self.parse)

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
        # duyệt qua các page
        # lấy năm của bài báo ở vị trí cuối page 
        date = int(response.css('div.details').css('p.date::text').get().split()[-1])
        next_page =  response.css('a.next.page-numbers').attrib['href'] 
        # nếu có page sau và bài báo cuối page từ năm 2018 trở đi thì tiếp tục duyêt page sau  
        if next_page is not None and date >= 2018:
            yield response.follow(next_page, callback=self.parse)

process = CrawlerProcess(settings={
    "FEEDS": {
        "is_sarcastic_v2.json": {"format": "json", 'encoding': 'utf8'},
    },
})


process.crawl(breitbartspider)
process.crawl(deadlinespider)
process.crawl(crikeyspider)
process.start()