#!/usr/bin/env python3

import requests

from base64 import b64encode
from bs4 import BeautifulSoup

class Utils:
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.76 Safari/537.36'}

    def get_HTML(file):
        f = open(file, 'r')
        lines = f.readlines()

        f.close()

        return("".join(lines))


    def fetch_source(url, stream=False):
        request = requests.get(url, headers=Utils.headers, stream=stream)
        if stream:
            return b64encode(request.content)
        return(request.text)
