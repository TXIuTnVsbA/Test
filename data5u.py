# -*- coding: utf-8 -*-
import requests,re
from lxml import etree
def getHtmlTree(url):
    html = requests.get(url, headers=HEADER).content
    return etree.HTML(html)

HEADER = {'Connection': 'keep-alive',
              'Cache-Control': 'max-age=0',
              'Upgrade-Insecure-Requests': '1',
              'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/537.36 (KHTML, like Gecko)',
              'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
              'Accept-Encoding': 'gzip, deflate, sdch',
              'Accept-Language': 'zh-CN,zh;q=0.8',
              }
url_list = ['http://www.data5u.com/',
                    'http://www.data5u.com/free/',
                    'http://www.data5u.com/free/gngn/index.shtml',
                    'http://www.data5u.com/free/gnpt/index.shtml']
for url in url_list:
    html_tree = getHtmlTree(url)
    ul_list = html_tree.xpath('//ul[@class="l2"]')
    for ul in ul_list:
        try:
            #yield ':'.join(ul.xpath('.//li/text()')[0:2])
            print ul.xpath('.//li/text()')[0:2]
        except Exception as e:
            pass
