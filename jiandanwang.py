#coding:utf-8

import requests
import urllib.request
from lxml import etree
import _md5
import hashlib
import base64
import time


def get_response(url,headers):

    response = requests.get(url,headers=headers)
    html = response.text
    # print(html)
    get_hash(html)

def get_hash(html):

    selector = etree.HTML(html)
    hashs = selector.xpath('//li/div/div/div[2]/p/span/text()')        #获取到图片的hash值
    # print(hashs)
    get_url(hashs)

# def get_js():
#     global r
#     js = 'http://cdn.jandan.net/static/min/91798e4c623fa60181a31d543488217e7f2ZE0GM.30100001.js'
#     r = 'zvvhmFaGE7I8FjdHv8XaZ5O6dmOltKa3'

def _md5(value):
    ''''md5加密'''
    m = hashlib.md5()
    m.update(value.encode('utf-8'))
    return m.hexdigest()


def _base64_decode(data):
    '''bash64解码'''
    missing_padding = 4 - len(data) % 4
    if missing_padding:
        data += '=' * missing_padding
    return base64.b64decode(data)


def get_url(hashs):
    for i in hashs:
        # print(i)
        get_imgurl(i,r)
        # time.sleep(2)


def get_imgurl(m,r='',d=0):

    '''解密获取图片链接'''
    e = "DECODE"
    q = 4
    r = _md5(r)
    o = _md5(r[0:0 + 16])
    n = _md5(r[16:16 + 16])
    l = m[0:q]
    c = o + _md5(o + l)
    m = m[q:]
    k = _base64_decode(m)
    url = k.decode('utf-8', errors='ignore')
    url = 'http://w' + url

    # print(url)

    download_img(url)

def download_img(url):
    # print(url)
    filename = url.split('/')[-1]
    opener = urllib.request.build_opener()

    try:
        opener.open(url)
        urllib.request.urlretrieve(url,'F:\\jiandan\\image\\' + filename)

    except urllib.error.HTTPError:
        print(url + '访问页面出错')
        # time.sleep(1)

    except urllib.error.URLError:
        print(url + '访问页面出错')
        # time.sleep(1)




if __name__ == '__main__':
    url_tg = 'http://jandan.net/ooxx'
    headers = {'user-agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'}

    #r这个参数我看了下是固定值
    r = 'zvvhmFaGE7I8FjdHv8XaZ5O6dmOltKa3'
    for i in range(1,45):
        url = url_tg + '/page-%s#comments'%i
        print('%s--------开始下载'%url)
        get_response(url,headers)
        print('%s--------下载完成'%url)
        time.sleep(10)
