#coding:utf8

import urllib
import re
from bs4 import BeautifulSoup
import requests,time
from urllib import quote

def get_html_baidu(url):
    headers = {'User-Agent':'Mozilla/5.0 (X11; U; Linux i686)Gecko/20071127 Firefox/2.0.0.11'}
    soup_baidu = BeautifulSoup(requests.get(url=url, headers=headers).content.decode('utf-8'), "lxml")

    # 去除无关的标签
    [s.extract() for s in soup_baidu(['script', 'style','img'])]
    print(soup_baidu.prettify())
    return soup_baidu

# soup_baidu = get_html_baidu('https://www.baidu.com/s?ie=utf-16&wd='+quote("天气"))
# soup_baidu = get_html_baidu('https://www.baidu.com/s?tn=mswin_oem_dg&ie=utf-16&word=%E5%A4%A9%E6%B0%94')
# print 123123
# print soup_baidu
# print 321321


headers = {'User-Agent':'Mozilla/5.0 (X11; U; Linux i686)Gecko/20071127 Firefox/2.0.0.11'}
print requests.get(url='https://www.baidu.com/s?tn=mswin_oem_dg&ie=utf-16&word=%E5%A4%A9%E6%B0%94', headers=headers).content.decode('utf-8')