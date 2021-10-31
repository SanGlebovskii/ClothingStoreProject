import scrapy

from clothspider.clothspider.items import ShoesSpiderItem


class ShoesSpider(scrapy.Spider):
    name = 'shoes'
    allowed_domains = ['by.wildberries.ru']
    start_urls = [
        'https://by.wildberries.ru/catalog/obuv/muzhskaya?sort=popular&page=1'
    ]

    def parse(self, response, **kwargs):
        for product in response.css('div.j-card-item'):
            link_to_product = product.css('a.j-open-full-product-card::attr(href)').get()
            yield response.follow(link_to_product, callback=self.parse_product)
        next_page = response.css('a.pagination-next').attrib['href']
        if next_page is not None:
            yield response.follow(next_page, callback=self.parse)

    def parse_product(self, response):
        product = response.css('div.main__container')

        for prod in product:
            pr_item = ShoesSpiderItem()
            category_id = 'shoess'
            price = prod.css('span.price-block__final-price::text').get()
            title = prod.css('h1.same-part-kt__header > span::text').get()
            descr = prod.css('div.j-description > p::text').get()
            composition = prod.css('div.j-consist::text').get()


            if price is not None:
                price = price.replace('\u00a0', '').replace('\u20bd', '').strip()
            else:
                price = 0

            pr_item['category'] = category_id
            pr_item['title'] = title
            pr_item['price'] = price
            pr_item['description'] = descr
            pr_item['composition'] = composition

            yield pr_item


