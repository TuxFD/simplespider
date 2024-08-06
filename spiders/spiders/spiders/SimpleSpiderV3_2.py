# ===========================================================
# TODO: Простейший скрипт Selenium + передать количество страниц парса в Scrapy через Bash
# NOTE: 57 pages, 24 items per page ~ 4 минуты
# ===========================================================

import re
import scrapy


DOMAIN = "https://shop.ms-armaturen.de/"
SORTING = "?order=m-s-artikelnummer-aufsteigend&p="


class SimpleSpiderV3(scrapy.Spider):
    name = "SimpleSpiderV3_2"
    allowed_domains = ["shop.ms-armaturen.de"]
    start_urls = []  # передаётся через bash
    custom_settings = {
        # "CONCURRENT_REQUESTS": 3,
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
    category_url = ""
    page_counter = 2

    def __init__(self, *args, **kwargs):
        super(SimpleSpiderV3, self).__init__(*args, **kwargs)
        self.start_urls = [kwargs.get("start_url")]
        # TODO: self.max_pages = [kwargs.get("max_pages")]

    def parse(self, response):
        if response.url not in self.visited_urls:
            self.visited_urls.append(response.url)

            products_table = False
            products_table = response.xpath("//tbody").extract()

            # парсим страницы товаров при наличии
            if products_table:
                self.category_url = self.get_category(
                    string=str(response.url), no_commas=True
                )
                for product_link in response.xpath("//tbody/tr/td/a/@href").extract():
                    yield response.follow(
                        product_link,
                        callback=self.parse_product,
                    )
                # переходим на следующие страницы внутри категории
                while self.page_counter < 58:
                    next_url = (
                        DOMAIN + self.category_url + SORTING + str(self.page_counter)
                    )
                    self.page_counter += 1
                    yield response.follow(next_url, callback=self.parse)

            # нет товаров - останавливаем парс без убийства паука
            else:
                return

    def get_category(self, string, no_commas=False):
        if no_commas:
            string1 = string.replace(DOMAIN, "").replace(SORTING, "")
        else:
            string1 = string.replace(DOMAIN, "").replace(SORTING, "").replace("/", ", ")
        string2 = re.sub(r"\d", "", string1).replace("b'", "").replace("'", "")
        return string2

    def parse_product(self, response):
        current_pr_category = ""
        refer_url = str(response.request.headers.get("Referer", None))
        current_pr_category = self.get_category(refer_url)

        pr_url = response.url
        pr_header = response.xpath(
            "//h1[@class='product-detail-name']/text()"
        ).extract()
        pr_articul = response.xpath(
            "//span[@class='product-detail-ordernumber']/text()"
        ).extract()
        pr_price = response.xpath("//p[@class='product-detail-price']/text()").extract()
        pr_stock = response.xpath(
            "//div[@class='product-detail-delivery-information']//p/text()"
        ).extract()
        pr_weight = response.xpath(
            "//span[@class='twt-product-detail-weight']/text()"
        ).extract()
        pr_pictures = response.xpath(
            "//div[@class='gallery-slider-thumbnails-item-inner']/img/@src"
        ).extract()
        pr_categories = current_pr_category

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
