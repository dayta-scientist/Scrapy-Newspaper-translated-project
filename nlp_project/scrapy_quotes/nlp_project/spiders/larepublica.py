import scrapy

class SpiderQuotes(scrapy.Spider):
    name = 'quotes'
    start_urls = [
        'https://www.larepublica.co/'
    ]
    custom_settings = {
        'FEED_URI': 'quotes.csv',
        'FEED_FORMAT': 'csv',
        'FEED_EXPORT_ENCODING': 'utf-8'
    }

    def parse(self, response):
            links = response.xpath('//text-fill[not(@class)]/a/@href').getall()
            for link in links:
                yield response.follow(link, callback=self.parse_link, cb_kwargs={'url': response.urljoin(link)})

    def parse_link(self, response, **kwargs):
        link = kwargs['url']
        title = response.xpath("//*[@id='vue-container']/div//h2/span/text()").get()
        #paragraph = response.xpath('//div[@class="field-item even"]//p[not(@class)]/text()').get()
        #body = response.xpath('//div[@class="body-nota"]/p/text()').getall()
        body = response.xpath('//div[@class="html-content"]/p[not(@class)]/text()').getall()

        yield {
            'url': link,
            'title': title,
            'body': body
        }