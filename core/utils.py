#!/usr/bin/env python3

import requests

from bs4 import BeautifulSoup

class Utils:
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.76 Safari/537.36'}

    def fetch_source(url):
        request = requests.get(url, headers=Utils.headers)

        return(request.text)
