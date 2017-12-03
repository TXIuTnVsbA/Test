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
#https://github.com/jhao104/proxy_pool
url = "http://www.goubanjia.com/free/gngn/index{page}.shtml"
for page in range(1, 10):
    page_url = url.format(page=page)
    tree = getHtmlTree(page_url)
    proxy_list = tree.xpath('//td[@class="ip"]')
    # 此网站有隐藏的数字干扰，或抓取到多余的数字或.符号
    # 需要过滤掉<p style="display:none;">的内容
    xpath_str = """.//*[not(contains(@style, 'display: none'))
                        and not(contains(@style, 'display:none'))
                        and not(contains(@class, 'port'))
                        ]/text()
                """
    for each_proxy in proxy_list:
        try:
            # :符号裸放在td下，其他放在div span p中，先分割找出ip，再找port
            ip_addr = ''.join(each_proxy.xpath(xpath_str))
            port = each_proxy.xpath(".//span[contains(@class, 'port')]/text()")[0]
            #yield '{}:{}'.format(ip_addr, port)
            print '{}:{}'.format(ip_addr, port)
        except Exception as e:
            pass
