#!/usr/bin/env python3

from core.utils import *
from core.crawler import *

class LCBOCrawler(Crawler):
    def crawl(self):
        dropddown_list = self.select('.nav .dropdown')

        for i in dropddown_list:
            # print(type(i))
            print(i.a.get_text())
            # print(i.ul)
            # print(type(i.ul))
            # print(.next())
            for a in i.ul.children:
                if type(a) is bs4.element.NavigableString: continue
                for b in a.children:
                    print(b)
                # print(type(a))
            # for j in i.ul.contents:
            #     if type(j) is bs4.element.NavigableString: continue
            #     print(j)
            #     break
            #     # print(type(j))

            break
