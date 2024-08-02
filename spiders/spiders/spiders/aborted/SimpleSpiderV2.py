import scrapy
from spiders.items import SpidersItem
# from scrapy.exceptions import CloseSpider
# from simple_config import CATEGORIES

MAINPAGE = "https://shop.ms-armaturen.de/"
SORTING = "?order=m-s-artikelnummer-aufsteigend&p="

CATEGORIES = [
    # "Rohrverbindungen/",
    "Rohrverbindungen/Verschraubungen/",
    "Rohrverbindungen/Flanschverbindungen/",
    "Rohrverbindungen/Clampverbindungen/",
    "Rohrverbindungen/Schlauchverbindungen/",
    "Rohrverbindungen/Industriefittings/",
]

# ===========================================================
# NOTE: start_urls обязательно содержит минимум 1 ссылку
# TODO: понять почему при нескольких ссылках start_urls запись в output.csv ломается
# TODO: как гонять паука по нескольким категориям сайта? (вытекает из предыдущего)
# ===========================================================


class SimpleSpiderV2(scrapy.Spider):
    name = "SimpleSpiderV2_dev"
    allowed_domains = ["shop.ms-armaturen.de"]
    start_urls = [
        "https://shop.ms-armaturen.de/Rohrverbindungen/Industriefittings/?order=m-s-artikelnummer-aufsteigend&p=1",
    ]
    visited_urls = []
    visited_categories = ["Rohrverbindungen/Industriefittings"]
    category_url = CATEGORIES[0]
    current_product_category = "Rohrverbindungen, Industriefittings, "

    def parse(self, response):
        # учёт посещённых ссылок
        if response.url not in self.visited_urls:
            self.visited_urls.append(response.url)

            products_table = False
            products_table = response.xpath("//tbody").extract()
            page404 = False
            page404 = response.xpath(
                "//h1[contains(text(), 'Seite nicht gefunden')]"
            ).extract()

            # парсим страницы товаров при наличии
            if products_table and not page404:
                for product_link in response.xpath("//tbody/tr/td/a/@href").extract():
                    yield response.follow(
                        product_link,
                        callback=self.parse_product,
                    )

                # переходим на следующие страницы внутри категории
                for i in range(2, 5):
                    next_url = response.url.replace("&p=1", "&p=" + str(i))
                    yield response.follow(next_url, callback=self.parse)

            # нет товаров - переходим к следующей категории
            else:
                # raise CloseSpider("End of products table!")
                for next_category in CATEGORIES:
                    # учёт отработанных категорий
                    if next_category not in self.visited_categories:
                        old_category = self.start_urls[0]
                        self.start_urls.append(old_category.replace(
                            self.category_url, next_category
                        ))
                        self.current_product_category = next_category.replace("/", ", ")

    def parse_product(self, response):
        item = SpidersItem()
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
        pr_categories = self.current_product_category

        item["pr_url"] = pr_url
        item["pr_header"] = pr_header
        item["pr_articul"] = pr_articul
        item["pr_price"] = pr_price
        item["pr_stock"] = pr_stock
        item["pr_weight"] = pr_weight
        item["pr_categories"] = pr_categories

        yield item
