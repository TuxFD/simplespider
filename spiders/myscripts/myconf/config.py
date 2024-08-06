# erasefile.py =================================
DEFAULT_FILENAME_ERASE = [
    "../spiders/files/raw/output_1.csv",
    "../spiders/files/raw/output_2.csv",
    "../spiders/files/raw/output_3.csv",
    '../spiders/files/temp/scrapy_output_1.log',
    '../spiders/files/temp/scrapy_output_2.log',
    '../spiders/files/temp/scrapy_output_3.log',
]


# prettyfile.py ================================
DEFAULT_FILENAME_PRETTYFILE = [
    "../spiders/files/raw/output_1.csv",
    "../spiders/files/raw/output_2.csv",
    "../spiders/files/raw/output_3.csv",
]
FILENAME_SUMMARY = "../spiders/files/cooked/output_summary.csv"
HEADERS = '"URL страницы","Заголовок","Артикул/SKU","Цена","Наличие","Вес","Картинки","Категории"\n'"
IN_STOCK_FALSE = "Bitte wenden Sie sich an Ihren zuständigen M&S Vertriebsmitarbeiter"
IN_STOCK_TRUE = "Auf Lager."


# urls_generator.py ============================
DOMAIN = "https://shop.ms-armaturen.de/"
SORTING = "?order=m-s-artikelnummer-aufsteigend&p="
CATEGORIES = [
    # "Rohrverbindungen/",
    "Rohrverbindungen/Verschraubungen/",
    "Rohrverbindungen/Flanschverbindungen/",
    "Rohrverbindungen/Clampverbindungen/",
    "Rohrverbindungen/Schlauchverbindungen/",
    "Rohrverbindungen/Industriefittings/",
]
