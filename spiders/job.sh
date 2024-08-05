#!/bin/sh

python3 myscripts/erasefile.py;
scrapy crawl SimpleSpiderV3_2 -o files/raw/output.csv -t csv;
python3 myscripts/prettyfile.py;