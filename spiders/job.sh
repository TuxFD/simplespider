#!/bin/sh

python3 myscripts/erasefile.py;
scrapy crawl SimpleSpiderV2 -o files/raw/output.csv -t csv;