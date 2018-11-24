#!/usr/bin/env python3

import re

from core.utils import *

from bs4 import BeautifulSoup

class ProductListing:
    def __init__(self, url):
        self.url = url
        self.crawl()

    def crawl(self):
        page_source = Utils.fetch_source(self.url)
        self.soup = BeautifulSoup(page_source, 'html.parser')

        print(self.soup.find(id='prodName').get_text())
        test = re.search(r'([0-9]+)', self.soup.find(id='prodSku').get_text(), re.I)
        if test:
            print(test.group())
