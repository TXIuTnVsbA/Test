# -*- coding: utf-8 -*-
import requests, re
from lxml import etree
HEADER = {'Connection': 'keep-alive',
          'Cache-Control': 'max-age=0',
          'Upgrade-Insecure-Requests': '1',
          'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/537.36 (KHTML, like Gecko)',
          'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
          'Accept-Encoding': 'gzip, deflate, sdch',
          'Accept-Language': 'zh-CN,zh;q=0.8',
          }
#url = 'http://www.ip3366.net/free/?stype=1&page=1'
#url = 'http://www.ip3366.net/free/?stype=2&page=1'
#url = 'http://www.ip3366.net/free/?stype=3&page=1'
url = 'http://www.ip3366.net/free/?stype=4&page=1'
html = requests.get(url, headers=HEADER).content
selector = etree.HTML(html)
xp = selector.xpath("//tr[td]")
regex = u"\d+\.\d+\.\d+\.\d+"
final_list = []
for tmp in xp:
    tmp_list = [i for i in tmp.itertext()]
    if re.findall(regex, tmp_list[1]):
        final_list.append(tmp_list[1] + ":" + tmp_list[3])

print final_list
