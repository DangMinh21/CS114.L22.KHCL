import scrapy
class wtopspider(scrapy.Spider):
    name = 'wtop'
    start_urls = ['https://wtop.com/local/',
                  'https://wtop.com/lifestyle/health-fitness/coronavirus/',
                  'https://wtop.com/national/',
                  'https://wtop.com/world/',
                  'https://wtop.com/business-finance/',
                  'https://wtop.com/government/',
                  'https://wtop.com/lifestyle/',
                  'https://wtop.com/sports/',
                  'https://wtop.com/entertainment/']

    def parse(self, response):
        for article in response.css('h3.post__template-title'):
            yield {
                'link': article.css('a').attrib['href'],
                'title': article.css('a::text').get(),
                'is_sarcsam': 0
            }
        next_page =  response.css('a.next.page-numbers').attrib['href']  
        if next_page is not None:
            yield response.follow(next_page, callback=self.parse)