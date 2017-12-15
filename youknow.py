# -*- coding: utf-8 -*-
import requests,os
from lxml import etree
import threading
import sys
requests.packages.urllib3.disable_warnings()
url_base="https://nhentai.net"
session = requests.Session()
session.headers.update({'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
                        'Accept-Language':'zh-cn,zh;q=0.8,en-us;q=0.5,en;q=0.3',
                        'User-agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:54.0) Gecko/20100101 Firefox/54.0'})

def spy_1(url,page_start,page, thread):
    # 首页一层
    #r=[]
    for tmp in range(page):
        html = str(session.get(url+str(page_start+tmp)).content)
        selector = etree.HTML(html)
        xp0 = selector.xpath(".//*[@id='content']/div[2]/div/a/@href")
        for tmp in xp0:
            #r.append(url_base + tmp)
            spy_2(url_base + tmp, thread)

def spy_2(url, thread):
    # 二层,本子预览
    #print url
    r=[]
    html = str(session.get(url).content)
    selector = etree.HTML(html)
    xp0=selector.xpath(".//*[@id='thumbnail-container']/div/a/@href")
    for tmp in xp0:
        r.append(spy_3(tmp))
        #r.append(url_base+tmp)
        #spy_3(url_base+tmp)
    if r:
        spy_Thread(r, thread, download)

def spy_3(url):
    # 三层,图片预览
    #print url
    url_tmp = url_base + url
    html = str(session.get(url_tmp).content)
    selector = etree.HTML(html)
    xp0 = selector.xpath(".//*[@id='image-container']/a/img/@src")
    print xp0
    if xp0:
        return xp0[0]
    return 0

def spy_Thread(list,maxpower = 16,target=None):
    #多线程
    i = 0
    result = []
    for tmp in list:
        i = i + 1
        try:
            #print tmp
            T = threading.Thread(target=target, args=(tmp,))
            T.start()
            result.append(T)
        except:
            pass
        if i % maxpower == 0:
            for tmp in result:
                tmp.join()
            del result[:]
    if result:
        for tmp in result:
            tmp.join()
        del result[:]

def download(url):
    #最后一层,下载图片,搞定
    print url
    tmp_dir=url.split("/")[-2]
    tmp_file=url.split("/")[-1]
    tmp_final=tmp_dir+"/"+tmp_file
    if os.path.exists(tmp_dir) == False:
        os.mkdir(tmp_dir)
    if  os.path.exists(tmp_final) == False:
        fp = open(tmp_final, 'wb')
        fp.write(session.get(url).content)
        fp.close()

if __name__ == '__main__':
    spy = "1"
    url = "https://nhentai.net/language/chinese/"
    page_start = 1
    page = 1
    thread = 32
    for i in range(1, len(sys.argv)):
        tmp = sys.argv[i].split("=")
        # print sys.argv[i].startswith('spy')
        if tmp[0] == "spy":
            spy = tmp[1]
        if tmp[0] == "url":
            url = tmp[1]
        if tmp[0] == "page_start":
            page_start = int(tmp[1])
        if tmp[0] == "page":
            page = int(tmp[1])
        if tmp[0] == "thread":
            thread = int(tmp[1])
        if tmp[0] == "help":
            print "spy=1 or 2\r\nurl=youknow\r\npage_start=1 or more\r\npage=1 or more\r\n|-page_start + page\r\nthread=2X\r\n"
            exit(0)
    if spy == "1-1":
    # 第一页起,遍历一页
        spy_1(url+"?page=", page_start, page, thread)
    if spy == "1-2":
    # 第一页起,遍历一页
        spy_1(url+"&page=", page_start, page, thread)
    if spy == "2-1":
        spy_2(url, thread)




