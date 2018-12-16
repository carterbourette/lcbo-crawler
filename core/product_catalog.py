#!/usr/bin/env python3

from core.crawler import *

class ProductCatalog(Crawler):

    def genURL(self, page_num):
        return('#contentBeginIndex=0&productBeginIndex=' + str((page_num - 1) * 12) + '&beginIndex=' + str((page_num - 1) * 12) + '&orderBy=&pageView=&resultType=products&orderByContent=&searchTerm=&facet=&storeId=10151&catalogId=10001&langId=-1&fromPage=&loginError=&userId=-1002&requesttype=ajax&objectId=')


    def crawl(self):
        page_counter = 1

        while True:
            products = self.select('.product')

            if len(products) <= 1:
                break

            for p in products:
                print(p.div.div.a['href'])
                print()

            page_counter += 1
            # self.load_page(self.url + self.genURL(page_counter))
            print(self.url + self.genURL(page_counter))
            break
