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
CATEGORY = "/Rohrverbindungen/"


class SimpleSpiderV3(scrapy.Spider):
    name = "SimpleSpiderV3_2"
    allowed_domains = ["shop.ms-armaturen.de"]
    start_urls = [
        # "Rohrverbindungen/", 24 items per page
        # "https://shop.ms-armaturen.de/Ventile/?order=m-s-artikelnummer-aufsteigend&p=19"
        # # "https://shop.ms-armaturen.de/Ventile/?order=m-s-artikelnummer-aufsteigend&p=12",
        # "https://shop.ms-armaturen.de/Ventile/?order=m-s-artikelnummer-aufsteigend&p=18"
        # # "https://shop.ms-armaturen.de/Rohrverbindungen/?order=m-s-artikelnummer-aufsteigend&p=19",
    ]
    custom_settings = {
        # "CONCURRENT_REQUESTS": 1,
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

    def parse(self, response):
        if response.url not in self.visited_urls:
            self.visited_urls.append(response.url)

            products_table = False
            products_table = response.xpath("//tbody").extract()

            self.category_url = self.get_category(
                string=str(response.url), no_commas=True
            )
            # парсим страницы товаров при наличии
            if products_table:
                for product_link in response.xpath("//tbody/tr/td/a/@href").extract():
                    yield response.follow(
                        product_link,
                        callback=self.parse_product,
                    )
            # нет товаров - останавливаем паука
            else:
                return  # останавливает парс без убийства паука
                # raise CloseSpider("End of products table!") # убивает паука

            # переходим на следующие страницы внутри категории
            i = 19
            while i < 20:
                next_url = DOMAIN + self.category_url + SORTING + str(i)
                i += 1
                yield response.follow(next_url, callback=self.parse)

    # def trouble_shooter(self, response):
    #     curr_url = str(response.url)
    #     counter = curr_url.count("https")
    #     if counter > 1:
    #         ...
    #     # yield response.follow(next_url, callback=self.parse)
    #     ...

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