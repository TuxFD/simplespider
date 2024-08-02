#!/bin/sh

python3 myscripts/erasefile.py;
scrapy crawl SimpleSpiderV3_1 -o files/raw/output_1.csv -t csv;