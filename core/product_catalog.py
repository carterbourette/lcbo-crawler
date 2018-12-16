#!/usr/bin/env python3

from core.crawler import *
from core.product_listing import *

class ProductCatalog(Crawler):

    def get_query_params(self, page_num):
        return {
          'contentBeginIndex': '0',
          'productBeginIndex': str((page_num - 1) * 12),
          'beginIndex': str((page_num - 1) * 12),
          'orderBy': '',
          'pageView': '',
          'resultType': 'products',
          'orderByContent': '',
          'searchTerm': '',
          'facet': '',
          'storeId': '10151',
          'catalogId': '10001',
          'langId': '-1',
          'fromPage': '',
          'loginError': '',
          'userId': '-1002',
          'objectId': '',
          'requesttype': 'ajax'
        }

    def crawl(self):
        page_counter = 1

        while True:
            products = self.select('.product')

            # When there are no more products, quit
            if len(products) < 1: break
            # TODO: Fix? We need to break if we're stuck in loop
            if page_counter > 300: break

            # Collect the individual links from catalog and create listing crawler
            for p in products:
                link = p.div.div.a['href']

                print('Create listing for ' + link)
                ProductListing(self.base_url + link).crawl()

            # When we are done the current page, request the next, rinse repeat
            page_counter += 1
            self.load_page(self.url, withAjax=True, payload=self.get_query_params(page_counter))
