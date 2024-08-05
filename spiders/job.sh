#!/bin/sh

python3 myscripts/erasefile.py;
scrapy crawl SimpleSpiderV3_2 -o files/raw/output.csv -t csv --logfile files/temp/scrapy_output.log;
python3 myscripts/prettyfile.py;