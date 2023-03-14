import scrapy


class SamsungSpider(scrapy.Spider):
    name = "samsung"
    allowed_domains = ["www.sikayetvar.com"]
    start_urls = ["http://www.sikayetvar.com/"]

    def parse(self, response):
        pass

# for porduct in products:
#     img_url = product.xpath('.//div[@class="image_container"]/a/img/@src').get()
#     book_name = product.xpath('//h3/a/text()').get()
#     book_price = product.xpath('//div[@class="product_price"]/p[@class="price_color"]/text()').get()
#     book_stock = product.xpath('//div[@class="product_price"]/p[@class="instock availability"]/text()').get()
#     print('image : ', img_url, '\nbook name : ', book_name, '\nbook price : ', book_price, '\nin stock : ', book_stock)


products = response.xpath('//article/@class["story-card complaint-card ga-v ga-c"]')

for product in products:
    title = product.xpath('.//section/h2[@class="complaint-title"]/a[@class="complaint-layer"]/text()').get()
    print("title : ", title)
    problem = product.xpath('.//section/p/text()').extract()
    print("Problem : ", problem[0])
