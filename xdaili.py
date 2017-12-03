# -*- coding: utf-8 -*-
import requests,re
from lxml import etree
HEADER = {'Connection': 'keep-alive',
              'Cache-Control': 'max-age=0',
              'Upgrade-Insecure-Requests': '1',
              'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/537.36 (KHTML, like Gecko)',
              'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
              'Accept-Encoding': 'gzip, deflate, sdch',
              'Accept-Language': 'zh-CN,zh;q=0.8',
              }
url = 'http://www.xdaili.cn/ipagent/freeip/getFreeIps?page=1&rows=10'
try:
    res =requests.get(url, headers=HEADER).json()
    for row in res['RESULT']['rows']:
        # yield '{}:{}'.format(row['ip'], row['port'])
        print '{}:{}'.format(row['ip'], row['port'])
except Exception as e:
    pass
