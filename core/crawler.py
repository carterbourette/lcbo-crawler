#!/usr/bin/env python3

import requests, bs4, time, random
from bs4 import BeautifulSoup
from base64 import b64encode, b64decode

class Crawler:
    def __init__(self, url):
        self.base_url = 'http://www.lcbo.com'
        self.url = url
        self.load_page(url)

    def load_page(self, url, withAjax=False, payload=None):
        # Add a delay between requests between (0..1)
        time.sleep(random.uniform(5, 20))
        self.url = url
        # Get the page source of the requested url
        page_source = Utils.fetch_source(self.url, withAjax=withAjax, payload=payload)
        self.soup = BeautifulSoup(page_source, 'html.parser')


    def select_one(self, select_string):
        selection = self.soup.select_one(select_string)
        if selection:
            return selection.get_text().strip()
        return selection


    def select(self, select_string):
        return self.soup.select(select_string)



class Utils:

    def get_HTML(file):
        f = open(file, 'r')
        lines = f.readlines()
        f.close()
        return("".join(lines))


    def fetch_source(url, stream=False, withAjax=False, payload=None):
        headers = { 'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.76 Safari/537.36'}
        try:
            if withAjax:
                headers['X-Requested-With'] = 'XMLHttpRequest'
                request = requests.post(url, data=payload, headers=headers)
            else:
                request = requests.get(url, headers=headers, stream=stream)
        except http.client.RemoteDisconnected:
            print('Remote disconnect, trying again...')
            return fetch_source(url, stream, withAjax=withAjax, payload=payload)

        if stream:
            return b64encode(request.content)
        return request.text


    def bs4_traverse_children(tag):
        for child in tag.contents:
            if type(child) is bs4.element.NavigableString: continue
            yield child
