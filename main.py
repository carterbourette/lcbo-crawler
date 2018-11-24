#!/usr/bin/env python3
#----------------------------------------------------------------------------
# Author      : Carter Bourette
# Description : A simple python web scraper.
#               ...
#----------------------------------------------------------------------------
#

from core.product_listing import *

if __name__ == "__main__":
    # print('Hello world!')
    #
    # headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.76 Safari/537.36'}
    #
    # # Request for listing page
    # # a = requests.get('http://www.lcbo.com/lcbo/catalog/ale/11022', headers=headers)
    # #
    # # soup = BeautifulSoup(a.text, 'html.parser')
    # #
    # # for product in soup.select(".category-search-title"):
    # #     print(product)
    #
    # a = requests.get('http://www.lcbo.com/lcbo/product/rickard-s-red/16907', headers=headers)
    #
    # soup = BeautifulSoup(a.text, 'html.parser')
    # #
    # # for product in soup.select("."):
    # #     print(product)
    #     # break
    #
    # print(soup.prettify())
    # # print(a.text)

    a = ProductListing('http://www.lcbo.com/lcbo/product/wells-ipa/439828')
