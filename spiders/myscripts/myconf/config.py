# erasefile.py =================================
DEFAULT_FILENAME_ERASE = [
    "../spiders/files/raw/output_1.csv",
    "../spiders/files/raw/output_2.csv",
    "../spiders/files/raw/output_3.csv",
    "../spiders/files/temp/scrapy_output_1.log",
    "../spiders/files/temp/scrapy_output_2.log",
    "../spiders/files/temp/scrapy_output_3.log",
]


# prettyfile.py ================================
DEFAULT_FILENAME_PRETTYFILE = [
    "../spiders/files/raw/output_1.csv",
    "../spiders/files/raw/output_2.csv",
    "../spiders/files/raw/output_3.csv",
]
FILENAME_SUMMARY = "../spiders/files/cooked/output_summary.csv"
HEADERS = '"URL страницы","Заголовок","Артикул/SKU","Цена","Наличие","Вес","Картинки","Категории"\n'
IN_STOCK_FALSE = "Bitte wenden Sie sich an Ihren zuständigen M&S Vertriebsmitarbeiter"
IN_STOCK_TRUE = "Auf Lager."

# selenium_spell.py ============================
FILENAME_SELENIUM = "../spiders/files/selenium_urls.txt"

# bash_generator.py ============================
FILENAME_BASH_JOB = "../spiders/job.sh"

# urls_generator.py ============================
FILENAME_FULLSITE_URLS = "../spiders/files/fullsite_urls.txt"
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
CATEGORIES_FULL = [
    # Rohrverbindungen
    "Rohrverbindungen/",
    "Rohrverbindungen/Verschraubungen/",
    "Rohrverbindungen/Flanschverbindungen/",
    "Rohrverbindungen/Clampverbindungen/",
    "Rohrverbindungen/Schlauchverbindungen/",
    "Rohrverbindungen/Industriefittings/",
    # Rohrformstuecke
    "Rohrformstuecke/",
    "Rohrformstuecke/Reduzierstuecke/",
    "Rohrformstuecke/Bogen/",
    "Rohrformstuecke/T-und-Kreuzstuecke/",
    # Scheiben-und-Kugelventile
    "Scheiben-und-Kugelventile/",
    "Scheiben-und-Kugelventile/Scheibenventile-Baureihe-SV04/",
    "Scheiben-und-Kugelventile/Scheibenventile-Classic/",
    "Scheiben-und-Kugelventile/Leckage-und-T-Scheibenventile/",
    "Scheiben-und-Kugelventile/Kugelventile/",
    "Scheiben-und-Kugelventile/Antriebe-Dichtungen-und-Zubehoer/",
    # Ventile
    "Ventile/",
    "Ventile/Sicherheitsventile/",
    "Ventile/Vakuumventile/",
    "Ventile/Tellerrueckschlagventile/",
    "Ventile/Probenahme-Eck-Drossel-Be-Entlueft/",
    # Zubehoer
    "Zubehoer/",
    "Zubehoer/Siebe/",
    "Zubehoer/Schauglaeser-und-laternen/",
    "Zubehoer/Behaelterarmaturen/",
    # Montagematerial
    "Zubehoer/Montagematerial/",
    # Rohrkappen
    "Zubehoer/Montagematerial/Rohrkappen/",
    "Zubehoer/Montagematerial/Rohrkappen/Rosette/",
    "Zubehoer/Montagematerial/Rohrkappen/Glocke/",
    "Zubehoer/Montagematerial/Rohrkappen/Gewoelbter-Boden/",
    "Zubehoer/Montagematerial/Kompensator/",
    # Kalottenfuesse
    "Zubehoer/Montagematerial/Kalottenfuesse/",
    "Zubehoer/Montagematerial/Kalottenfuesse/komplett/",
    "Zubehoer/Montagematerial/Kalottenfuesse/Kalottenfuss/",
    "Zubehoer/Montagematerial/Kalottenfuesse/Kalottenmuffe/",
    "Zubehoer/Montagematerial/Kalottenfuesse/Kalottenteller/",
    "Zubehoer/Montagematerial/Kalottenfuesse/Kalottenmutter/",
    "Zubehoer/Montagematerial/Rohrschellen/",
    "Zubehoer/Montagematerial/Rohrspannbuegel/",
    "Zubehoer/Montagematerial/Rohrschlitten/",
    # Werkzeug
    "Zubehoer/Montagematerial/Werkzeug/",
    "Zubehoer/Montagematerial/Werkzeug/Rohrwalze/",
    "Zubehoer/Montagematerial/Werkzeug/Rohrsaegewerkzeug/",
    "Zubehoer/Montagematerial/Werkzeug/Hakenschluessel/",
    # Hygienearmaturen
    "Hygienearmaturen/",
    "Hygienearmaturen/Verschraubungen/",
    "Hygienearmaturen/Flanschverbindungen/",
    "Hygienearmaturen/Klemmverbindungen/",
    "Hygienearmaturen/TC-Verbindungen/",
    "Hygienearmaturen/Bogen/",
    "Hygienearmaturen/Reduzierstuecke/",
    "Hygienearmaturen/Dichtungen/",
    "Hygienearmaturen/T-Stuecke/",
]
