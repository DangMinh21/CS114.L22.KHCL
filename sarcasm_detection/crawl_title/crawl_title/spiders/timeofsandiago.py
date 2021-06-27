import scrapy
class timeofsandiagospider(scrapy.Spider):
    name = 'timeofsandiago'
    start_urls = ['https://timesofsandiego.com/archives-2/page/417/']

    def parse(self, response):
        for article in  response.css('h2.entry-title'):
            yield {
                'link': article.css('a').attrib['href'],
                'title': article.css('a::text').get(),
                'is_sarcsam': 0
            }
        year = int(response.css('time.entry-date.published')[-1].attrib['datetime'].split('-')[0])
        next_page =  response.css('a.next.page-numbers').attrib['href']  
        if next_page is not None and year > 18:
            yield response.follow(next_page, callback=self.parse)