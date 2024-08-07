#!/bin/sh
python3 myscripts/erasefile.py;
scrapy crawl SimpleSpiderV3_2 -a start_url="https://shop.ms-armaturen.de/Rohrverbindungen/?order=m-s-artikelnummer-aufsteigend&p=1" -a maxpage="3" -o files/raw/output_1.csv:csv --logfile files/temp/scrapy_output_1.log;

python3 myscripts/prettyfile.py;
