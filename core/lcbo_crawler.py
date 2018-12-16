#!/usr/bin/env python3

from core.crawler import *
from core.product_catalog import *

class LCBOCrawler(Crawler):

    def crawl(self):
        dropdown_list = self.select('.nav .dropdown')

        visit_map = {}
        # For each menu item in the homepage header
        for dd in dropdown_list:
            # Get the menu header name - this will be our main category
            parent = dd.a.get_text()

            # TODO: Make more generic
            # if parent not in ['Coolers', 'Beer & Cider', 'Spirits', 'Wine']: continue
            if parent not in ['Beer & Cider']: continue
            print(parent)

            # If there is no submenu, just move on
            if not dd.ul: continue

            visit_map[parent] = []

            # Otherwise, traverse the menu and fetch the categories
            for li in Utils.bs4_traverse_children(dd.ul):
                category = li.a.get_text()
                print('\t' + category)

                # Further menus
                if li.ul:
                    for ul_li in Utils.bs4_traverse_children(li.ul):
                        subcategory = ul_li.a.get_text()
                        print('\t\t' + subcategory)
                        visit_map[parent].append({ 'top': category, 'target': subcategory, 'src': ul_li.a['href'] })

                # We're at the bottom layer
                else:
                    visit_map[dd.a.get_text()].append({ 'top': category, 'target': category, 'src': li.a['href'] })

        # Let's just write out the links to visit
        for key in visit_map.keys():

            # TODO: Create product top level category
            print(key)

            for m in visit_map[key]:

                # We want to skip the 'All' pages
                if m['top'] == 'Show All': continue

                # TODO: Create product sub level category as category and subcategory

                # Run the catalog crawler using the catalog url
                # NOTE: remove the last 7 chars, /lcbo/catalog/bock/11090
                src = m['src'][:-7]
                print('Creating catalog for ' + src)
                ProductCatalog(self.base_url + src).crawl()
