import scrapy
class thedailyerspider(scrapy.Spider):
    name = 'thedailyer'
    start_urls = ['http://thedailyer.com/category/feat/']

    def parse(self, response):
        for article in response.css('h1.title.entry-title > a'):
            yield {
                'link': article.attrib['href'],
                'title': article.css('::text').get(),
                'is_sarcsam': 1
            }
        date_string = response.css('li.published.updated')[-1].css('a::text').get().split()[-1]
        year = int(date_string)
        next_page = response.css('a.button')[-1].attrib['href']    
        if next_page is not None and year >= 2017:
            yield response.follow(next_page, callback=self.parse)