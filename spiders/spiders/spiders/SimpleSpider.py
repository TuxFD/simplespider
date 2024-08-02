import scrapy
from spiders.items import SpidersItem

# from spiders.spiders.simple_config import CATEGORIES  # , CUSTOM_FIELDS

# ===========================================================
CATEGORIES = [
    "Rohrverbindungen/Industriefittings/",
]
# ===========================================================


class SimpleSpider(scrapy.Spider):
    start_urls = ["https://shop.ms-armaturen.de/"]
    name = "SimpleSpider"
    allowed_domains = ["shop.ms-armaturen.de"]
    # start_urls = []
    visited_urls = []

    def parse(self, responce):
        print("AFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF")

        self.genurls()  # набиваем ссылки для парса

        if responce.url not in self.visited_urls:  # учёт посещённых ссылок
            self.visited_urls.append(responce.url)

        #     for product_link in responce.xpath(
        #         # '//div[@class="post mb-2"]/h2/a/@href'
        #         "//tbody/tr/td/a/@href"
        #     ).extract():  # обработка страниц товаров
        #         yield responce.follow(product_link, callback=self.parse_product)

    def setfields(self):
        item = SpidersItem()

        item["pr_url"] = "111"
        # item["pr_header"] = "111"
        # item["pr_articul"] = "111"
        # item["pr_price"] = "111"
        # item["pr_stock"] = "111"
        # item["pr_weight"] = "111"
        # item["pr_categories"] = "111"

        # item["pr_url"] = CUSTOM_FIELDS[0]
        # item["pr_header"] = CUSTOM_FIELDS[1]
        # item["pr_articul"] = CUSTOM_FIELDS[2]
        # item["pr_price"] = CUSTOM_FIELDS[3]
        # item["pr_stock"] = CUSTOM_FIELDS[4]
        # item["pr_weight"] = CUSTOM_FIELDS[5]
        # item["pr_categories"] = CUSTOM_FIELDS[6]

        yield item

    def parse_product(self, responce):
        item = SpidersItem()

        # pr_url = responce.xpath("").extract()
        pr_header = responce.xpath("").extract()
        # pr_articul = responce.xpath("").extract()
        # pr_price = responce.xpath("").extract()
        # pr_stock = responce.xpath("").extract()
        # pr_weight = responce.xpath("").extract()
        # pr_categories = responce.xpath("").extract()

        # item["pr_url"] = pr_url
        item["pr_header"] = pr_header
        # item["pr_articul"] = pr_articul
        # item["pr_price"] = pr_price
        # item["pr_stock"] = pr_stock
        # item["pr_weight"] = pr_weight
        # item["pr_categories"] = pr_categories

        yield item
        print(item)

    def genurls(self):
        self.start_urls.clear()
        for category in CATEGORIES:
            print(category)
            for i in range(1, 2):
                url = (
                    "https://"
                    + self.allowed_domains[0]
                    + category
                    + "?order=m-s-artikelnummer-aufsteigend&p="
                    + str(i)
                )
                self.start_urls.append(url)
                print(url)
