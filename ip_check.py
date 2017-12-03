# -*- coding: utf-8 -*-
import requests,re
import IPy as ipy
from lxml import etree
import threading
from multiprocessing import Pool
import threadpool
import time
requests.packages.urllib3.disable_warnings()
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
    return re.findall(r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}:\d{1,5}', html)
    #for proxy in re.findall(r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}:\d{1,5}', html):
        #Online_CheckProxy_Custom(proxy)
        #print proxy
def check_138_com(proxies=None):
    header={"Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
            "User-Agent":"Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36"}
    # proxies = {'http':'http://localhost:8888','https':'https://localhost:8888'} #debug
    # proxies = {'http':'http://localhost:8087','https':'https://localhost:8087'} #debug
    try:
        url_ip138 = 'http://2017.ip138.com/ic.asp'
        r = str(requests.get(url=url_ip138,headers=header, timeout=3, proxies=proxies).content)
        selector = etree.HTML(r)
        xp0 = selector.xpath("//body/center")
        if xp0:
            regex = u"\d+\.\d+\.\d+\.\d+"
            if re.findall(regex, xp0[0].text):
                return 1
    except:
        return 0
def check_ip_cn(proxies=None):
    header = {"Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
              "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36"}
    try:
        url = 'http://ip.cn'
        r = str(requests.get(url=url,headers=header, timeout=3, proxies=proxies).content)
        selector = etree.HTML(r)
        xp0 = selector.xpath("//div[@id='result']/div/p/code")
        if xp0:
            regex = u"\d+\.\d+\.\d+\.\d+"
            if re.findall(regex, xp0[0].text):
                return 1
    except:
        return 0
def check_proxy(ip,port):
    proxies = {
                'http': 'http://{text1}:{text2}'.format(text1=ip,text2=port),
                'https': 'https://{text1}:{text2}'.format(text1=ip,text2=port)
    }
    if check_ip_cn(proxies):
        out(str(ip)+':'+str(port))
        return
    if check_138_com(proxies):
        out(str(ip) + ':' + str(port))
        return
    return
def check_proxy_link(proxy):
    proxies = {
        'http': 'http://{text1}'.format(text1=proxy),
        'https': 'https://{text1}'.format(text1=proxy)
    }
    if check_ip_cn(proxies):
        #out(proxy)
        out(str(proxy))
        return
    if check_138_com(proxies):
        #out(proxy)
        out(str(proxy))
        return
    return
def out_tmp(text):
    with open(r'out_ip_tmp.txt', 'a') as fp:
        fp.writelines(str(text).replace('\r',''))
def out(str):
    now=time.strftime('%Y%m%d',time.localtime(time.time()))
    try:
        fp = open(r'ip_'+now+".txt", "r")
        tmp=fp.read()
        fp = open(r'ip_'+now+".txt", "a")
        if(tmp.find(str)==-1):
            fp.write(str+'\n')
        fp.close()
    except:
        fp=open(r'ip_'+now+".txt", "a")
        fp.write(str+'\n')
        fp.close()
def main():
    pool = Pool(64)
    result = []
    ip = ipy.IP('111.13.15.0/24')
    for x in ip:
        #print x
        try:
            #result.append(pool.apply_async(check_proxy, (x,80)))
            #pool.apply_async(check_proxy_link, args=(x['http'],))
            pool.apply_async(check_proxy, (x, 80))
        except:
            pass

    pool.close()
    pool.join()
    #for res in result:
    #    print res.get()
    print "Sub-process(es) done."
def test():
    pool = Pool(10)
    with open(r'D:\python\iproutes.txt', 'r') as fp:
        for tmp in fp.readlines():
            #print tmp
            result = []
            ip = ipy.IP(tmp)
            for x in ip:
                print x
                try:
                    result.append(pool.apply_async(check_proxy, (x,80)))
                    # pool.apply_async(check_proxy_link, args=(x['http'],))
                    #pool.apply_async(check_proxy, (x, 80))
                    #pool.apply(check_proxy, (x,80))
                except:
                    pass
            for tmp in result:
                tmp.get()
            del result[:]
            print '\r\n=======================================================================================\r\n'
    pool.close()
    pool.join()
    # for res in result:
    #    print res.get()
    print "Sub-process(es) done."
def test1():
    pool = 2048
    with open(r'D:\python\iproutes.txt', 'r') as fp:
        for tmp in fp.readlines():
            #print tmp
            i = 0
            result = []
            ip = ipy.IP(tmp)
            for x in ip:
                i=i+1
                print x
                #print i,len(result)
                try:
                    T=threading.Thread(target=check_proxy,args=(x,80))
                    T.start()
                    result.append(T)
                    #result.append(pool.apply_async(check_proxy, (x,80)))
                    # pool.apply_async(check_proxy_link, args=(x['http'],))
                    #pool.apply_async(check_proxy, (x, 80))
                    #pool.apply(check_proxy, (x,80))
                except:
                    pass
                if i % pool == 0:
                    #print 'join'
                    for tmp in result:
                        tmp.join()
                    del result[:]
            #print len(result)
            if result:
                for tmp in result:
                    tmp.join()
                del result[:]
            print '=======================================================================================\r\n'
    #pool.close()
    #pool.join()
    # for res in result:
    #    print res.get()
    #print "Sub-process(es) done."
def test2(proxy_number=10,port=80):
    maxpower = 2048
    i = 0
    result = []
    for tmp in GetProxy_66ip(proxy_number,port):
        i = i + 1
        print tmp
        try:
            T = threading.Thread(target=check_proxy_link, args=(tmp, ))
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


if __name__ == '__main__':
    #main()
    #Q=Queue.Queue(255)
    #test1()
    while True:
        test2(100,0)
        #time.sleep(5)
