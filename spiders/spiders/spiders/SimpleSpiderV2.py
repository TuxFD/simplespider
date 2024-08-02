import re
import scrapy
from spiders.items import SpidersItem

MAINPAGE = "https://shop.ms-armaturen.de/"
SORTING = "?order=m-s-artikelnummer-aufsteigend&p="


class SimpleSpiderV2(scrapy.Spider):
    """scrapy crawl SimpleSpiderV2 -o files/raw/output.csv -t csv"""

    name = "SimpleSpiderV2"
    allowed_domains = ["shop.ms-armaturen.de"]
    start_urls = [
        "https://shop.ms-armaturen.de/Rohrverbindungen/Industriefittings/?order=m-s-artikelnummer-aufsteigend&p=1",
        # "https://shop.ms-armaturen.de/Zubehoer/Montagematerial/Rohrkappen/Rosette/?order=m-s-artikelnummer-aufsteigend&p=1",
    ]  # обязателен! минимум 1 ссылка!
    visited_urls = []
    current_category = ""

    # def __init__(self):
    #     self.erasefile()  # очистить файл output.csv

    def parse(self, response):
        if response.url not in self.visited_urls:  # учёт посещённых ссылок
            self.visited_urls.append(response.url)
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

            for product_link in response.xpath("//tbody/tr/td/a/@href").extract():
                yield response.follow(
                    product_link,
                    callback=self.parse_product,
                )

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
