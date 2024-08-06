#!/bin/sh

python3 myscripts/erasefile.py;

scrapy crawl SimpleSpiderV3_2 -a start_url="https://shop.ms-armaturen.de/Ventile/Sicherheitsventile/?order=m-s-artikelnummer-aufsteigend&p=1" -o files/raw/output_1.csv -t csv --logfile files/temp/scrapy_output_1.log & scrapy crawl SimpleSpiderV3_2 -a start_url="https://shop.ms-armaturen.de/Ventile/Vakuumventile/?order=m-s-artikelnummer-aufsteigend&p=1" -o files/raw/output_2.csv -t csv --logfile files/temp/scrapy_output_2.log & scrapy crawl SimpleSpiderV3_2 -a start_url="https://shop.ms-armaturen.de/Zubehoer/Siebe/?order=m-s-artikelnummer-aufsteigend&p=1" -o files/raw/output_3.csv -t csv --logfile files/temp/scrapy_output_3.log && fg;

python3 myscripts/prettyfile.py;

# ===========================================================
# TODO: Простейший скрипт Selenium + передать количество страниц парса в Scrapy через Bash
# ===========================================================