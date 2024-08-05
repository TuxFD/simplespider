# ===========================================================
# NOTE: start_urls обязательно содержит минимум 1 ссылку
# TODO: понять почему при нескольких ссылках start_urls запись в output.csv ломается
# TODO: как гонять паука по нескольким категориям сайта? (вытекает из предыдущего)
# ===========================================================


import re
import scrapy
# from scrapy.exceptions import CloseSpider

CATEGORIES = []
DOMAIN = "https://shop.ms-armaturen.de/"
SORTING = "?order=m-s-artikelnummer-aufsteigend&p="


class SimpleSpiderV3(scrapy.Spider):
    name = "SimpleSpiderV3_2"
    allowed_domains = ["shop.ms-armaturen.de"]
    start_urls = [
        # "https://shop.ms-armaturen.de/Rohrverbindungen/Verschraubungen/?order=m-s-artikelnummer-aufsteigend&p=1",
        # "https://shop.ms-armaturen.de/Hygienearmaturen/T-Stuecke/?order=m-s-artikelnummer-aufsteigend&p=2",
        "https://shop.ms-armaturen.de/Zubehoer/Behaelterarmaturen/?order=m-s-artikelnummer-aufsteigend&p=4",
    ]
    custom_settings = {
        # "CONCURRENT_REQUESTS": 2,
        "FEED_EXPORT_FIELDS": [
            "URL страницы",
            "Заголовок",
            "Артикул/SKU",
            "Цена",
            "Наличие",
            "Вес",
            "Картинки",
            "Категории",
        ],
    }
    visited_urls = []
    current_pr_category = ""

    def parse(self, response):
        if response.url not in self.visited_urls:
            self.visited_urls.append(response.url)

            products_table = False
            products_table = response.xpath("//tbody").extract()

            # парсим страницы товаров при наличии
            if products_table:
                self.current_pr_category = self.get_category(str(response.url))
                for product_link in response.xpath("//tbody/tr/td/a/@href").extract():
                    yield response.follow(
                        product_link,
                        callback=self.parse_product,
                    )

            # # переходим на следующие страницы внутри категории
            # for i in range(2, 35):
            #     curr_url = str(response.url)
            #     next_url = curr_url.replace("&p=1", "&p=" + str(i))
            #     yield response.follow(next_url, callback=self.parse)

            # нет товаров - останавливаем паука
            # else:
            #     raise CloseSpider("End of products table!")

    def get_category(self, string):
        string1 = string.replace(DOMAIN, "").replace(SORTING, "").replace("/", ", ")
        string2 = re.sub(r"\d", "", string1)
        return string2

    def parse_product(self, response):
        pr_url = response.url
        pr_header = response.xpath(
            "//h1[@class='product-detail-name']/text()"
        ).extract()
        pr_articul = (
            response.xpath("//span[@class='product-detail-ordernumber']/text()")
            .extract()
        )
        pr_price = (
            response.xpath("//p[@class='product-detail-price']/text()")
            .extract()
        )
        pr_stock = response.xpath(
            "//div[@class='product-detail-delivery-information']//p/text()"
        ).extract()
        pr_weight = (
            response.xpath("//span[@class='twt-product-detail-weight']/text()")
            .extract()
        )
        pr_pictures = response.xpath(
            "//div[@class='gallery-slider-thumbnails-item-inner']/img/@src"
        ).extract()
        pr_categories = self.current_pr_category

        yield {
            "URL страницы": pr_url,
            "Заголовок": pr_header,
            "Артикул/SKU": pr_articul,
            "Цена": pr_price,
            "Наличие": pr_stock,
            "Вес": pr_weight,
            "Картинки": pr_pictures,
            "Категории": pr_categories,
        }
