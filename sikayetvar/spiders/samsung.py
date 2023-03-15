import scrapy


class SamsungSpider(scrapy.Spider):
    name = "samsung"
    allowed_domains = ["www.sikayetvar.com"]
    start_urls = ["https://www.sikayetvar.com/samsung-telefon?page=1"]

    def parse(self, response):
        products = response.xpath('//article[@class="story-card complaint-card ga-v ga-c"]')
        for product in products:
            yield { 'title' : product.xpath('.//section/h2[@class="complaint-title"]/a[@class="complaint-layer"]/text()').get(),
                   'problem': product.xpath('.//section/p/text()').extract()}
         # Bir sonraki sayfayı oluşturun
        next_page_number = int(response.url.split("=")[-1]) + 1
        next_page_url = f"https://www.sikayetvar.com/samsung-telefon?page={next_page_number}"
    
        # Bir sonraki sayfaya istek gönderin
        yield scrapy.Request(next_page_url, callback=self.parse)   

