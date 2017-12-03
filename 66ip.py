# -*- coding: utf-8 -*-
import requests,re
def GetProxy_66ip(proxy_number=10,port=80):
    HEADER = {'Connection': 'keep-alive',
              'Cache-Control': 'max-age=0',
              'Upgrade-Insecure-Requests': '1',
              'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/537.36 (KHTML, like Gecko)',
              'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
              'Accept-Encoding': 'gzip, deflate, sdch',
              'Accept-Language': 'zh-CN,zh;q=0.8',
              }
    #url = "http://www.66ip.cn/mo.php?sxb=&tqsl={}&port=80".format(proxy_number)
    url="http://www.66ip.cn/mo.php?sxb=&tqsl={num}&port={por}&export=&ktip=&sxa=&submit=%CC%E1++%C8%A1&textarea=".format(num=proxy_number,por=str(port))
    html = requests.get(url, headers=HEADER).content
    #return re.findall(r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}:\d{1,5}', html)
    for proxy in re.findall(r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}:\d{1,5}', html):
        #Online_CheckProxy_Custom(proxy)
        print proxy

GetProxy_66ip()
