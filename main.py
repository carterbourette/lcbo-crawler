#!/usr/bin/env python3
#----------------------------------------------------------------------------
# Author      : Carter Bourette
# Description : A simple python web scraper.
#               ...
#----------------------------------------------------------------------------
#

from core.product_listing import *
from core.lcbo_crawler import *
from core.product_catalog import *

if __name__ == "__main__":

    LCBOCrawler('http://www.lcbo.com/content/lcbo/en.html').crawl()
