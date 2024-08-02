# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class SpidersItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pr_url = scrapy.Field()
    pr_header = scrapy.Field()
    pr_articul = scrapy.Field()
    pr_price = scrapy.Field()
    pr_stock = scrapy.Field()
    pr_weight = scrapy.Field()
    pr_categories = scrapy.Field()
    # pass


# CUSTOM_FIELDS = [
#     "URL страницы",
#     "Заголовок",
#     "Артикул/SKU",
#     "Цена",
#     "Наличие",
#     'Вес',
#     "Категории",
# ]
