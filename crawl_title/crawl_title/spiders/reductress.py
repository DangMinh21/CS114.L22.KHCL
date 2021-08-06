import scrapy
class reductressspider(scrapy.Spider):
    name = 'reductress'
    start_urls = ['https://reductress.com/news/page/1/']

    def parse(self, response):
        for article in   response.css('div.box'):
            yield {
                'link': article.css('a').attrib['href'],
                'title': article.css('a').attrib['title'],
                'is_sarcsam': 1
            }
        date = int(response.css('div.box')[0].css('a').css('img').attrib['src'].split('/')[5])
        next_page =response.css('a.next.page-numbers').attrib['href']   
        if next_page is not None and date >= 2017:
            yield response.follow(next_page, callback=self.parse)