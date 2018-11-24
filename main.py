#!/usr/bin/env python3
#----------------------------------------------------------------------------
# Author      : Carter Bourette
# Description : A simple python web scraper.
#               ...
#----------------------------------------------------------------------------
#

from core.product_listing import *
from core.lcbo_crawler import *

if __name__ == "__main__":
    # ProductListing('http://www.lcbo.com/lcbo/product/rickard-s-red/16907#.W_jbcmhKiUk').crawl()
    # ProductListing('http://www.lcbo.com/lcbo/product/creemore-springs-pale-wheat/575175#.W_mD32hKiUk')

    LCBOCrawler('http://www.lcbo.com/content/lcbo/en.html').crawl()
