import re
import scrapy
from spiders.items import SpidersItem
from scrapy.exceptions import CloseSpider
from simple_config import CATEGORIES

MAINPAGE = "https://shop.ms-armaturen.de/"
SORTING = "?order=m-s-artikelnummer-aufsteigend&p="


class SimpleSpiderV2(scrapy.Spider):
    """scrapy crawl SimpleSpiderV2 -o files/raw/output.csv -t csv"""

    name = "SimpleSpiderV2"
    allowed_domains = ["shop.ms-armaturen.de"]
    # TODO: понять почему при нескольких ссылках запись в output.csv ломается
    start_urls = [
        "https://shop.ms-armaturen.de/Rohrverbindungen&p=1",  # обязателен! минимум 1 ссылка!
    ]
    visited_urls = []
    current_category = ""

    def parse(self, response):
        if response.url not in self.visited_urls:  # учёт посещённых ссылок
            self.visited_urls.append(response.url)

            products_table = False
            products_table = response.xpath("//tbody").extract()

            if products_table:
                category = (
                    str(response.url)
                    .replace(MAINPAGE, "")
                    .replace(SORTING, "")
                    .replace("/", ", ")
                )
                category = re.sub("\d+", "", category)
                self.current_category = category
                catd = dict()
                catd["0"] = category
                print(category)

                for product_link in response.xpath(
                    "//tbody/tr/td/a/@href"
                ).extract():  # парсим страницы товаров
                    yield response.follow(
                        product_link,
                        callback=self.parse_product,
                    )
                # переходим на следующие страницы
                for i in range(2, 5):
                    next_url = response.url.replace("&p=1", "&p=" + str(i))
                    yield response.follow(next_url, callback=self.parse)
            else:
                raise CloseSpider("End of products table!")

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
        pr_categories = self.current_category

        item["pr_url"] = pr_url
        item["pr_header"] = pr_header
        item["pr_articul"] = pr_articul
        item["pr_price"] = pr_price
        item["pr_stock"] = pr_stock
        item["pr_weight"] = pr_weight
        item["pr_categories"] = pr_categories

        yield item
