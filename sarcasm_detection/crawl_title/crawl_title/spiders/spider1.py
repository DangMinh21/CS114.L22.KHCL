import scrapy
from scrapy.crawler import CrawlerProcess
# gôm 3 class tưng ứng với 3 trang báo 
class chaserspider(scrapy.Spider):
    name = 'chaser'
    start_urls = ['https://chaser.com.au/news']

    def parse(self, response):
        for article in  response.css('div.container').css('a')[0:10]:
            yield {
                'article_link': article.attrib['href'],
                'headline': article.css('div.archive_story_title::text').get(),
                'is_sarcastic': 1
            }
        # duyệt qua các page
        # lấy năm của bài báo ở vị trí cuối page 
        date = int(response.css('div.container').css('a')[9].css('time.entry-date').attrib['datetime'].split('-')[0])
        next_page = response.css('div.container').css('a')[10].attrib['href']  
        # nếu có page sau và bài báo cuối page từ năm 2018 trở đi thì tiếp tục duyêt page sau
        if next_page is not None and date >= 2018:
            yield response.follow(next_page, callback=self.parse)

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
        # duyệt qua các page
        # lấy năm của bài báo ở vị trí cuối page 
        date = int(response.css('time.time')[-1].attrib['datetime'].split('-')[0])
        next_page =response.css('a.next.page-numbers').attrib['href']  
        # nếu có page sau và bài báo cuối page từ năm 2018 trở đi thì tiếp tục duyêt page sau 
        if next_page is not None and date >= 2018:
            yield response.follow(next_page, callback=self.parse)

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
        # duyệt qua các page
        # lấy năm của bài báo ở vị trí cuối page 
        date = int( response.css('div.post-header').css('div.post-byline::text')[-1].get().split()[-1])
        next_page = response.css('a.next.page-numbers').attrib['href'] 
        # nếu có page sau và bài báo cuối page từ năm 2018 trở đi thì tiếp tục duyêt page sau
        if next_page is not None and date >= 2018:
            yield response.follow(next_page, callback=self.parse)

process = CrawlerProcess(settings={
    "FEEDS": {
        "is_sarcastic.json": {"format": "json", 'encoding': 'utf8'},
    },
})

# thực thi crawl
process.crawl(chaserspider)
process.crawl(beavertonspider)
process.crawl(clickholespider)
process.start()