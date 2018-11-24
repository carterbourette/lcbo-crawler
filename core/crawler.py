#!/usr/bin/env python3

from core.utils import *

import bs4
from bs4 import BeautifulSoup

class Crawler:
    def __init__(self, url):
        self.url = url

        page_source = Utils.get_HTML('homepage.html')
        # page_source = Utils.fetch_source(self.url)
        self.soup = BeautifulSoup(page_source, 'html.parser')


    def select_one(self, select_string):
        selection = self.soup.select_one(select_string)
        if selection:
            return selection.get_text().strip()
        return selection


    def select(self, select_string):
        return self.soup.select(select_string)
