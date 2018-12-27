#!/usr/bin/python3
# -*- coding: utf-8 -*-
import requests
import time
import re
import os
import random
import logging
from bs4 import BeautifulSoup

logger = logging.getLogger(__name__)
fh = logging.FileHandler(encoding='utf-8', mode='a', filename="t.log")
logging.basicConfig(handlers=[fh], format='[%(asctime)s %(levelname)s]<%(process)d> %(message)s',\
 datefmt='%Y-%m-%d %H:%M:%S', level=logging.DEBUG)

headers_post = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "zh-CN,zh;q=0.9",
    "content-type": "application/x-www-form-urlencoded",
    "origin": "https://sobooks.net",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) \
    AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36",
    "Connection": "keep-alive"
}
ss = requests.session()
ss.headers.update(headers_post)
path = os.getcwd()
down_list_file = os.path.join(path, "downurl_lists.txt")

code = {"e_secret_key": "2018919"}
reString = re.compile(r'.*(http[s]?://pan.baidu.*)')

for j in range(166):
    try:
        url_list = []
        j += 1
        logger.info('downloading page {0}'.format(j))
        url = 'https://sobooks.net/page/' + str(j)
        r = ss.get(url, headers=headers_post)
        html = r.text
        soup = BeautifulSoup(html, "html.parser")
        bookurl_list = soup.find_all("h3")
        a = [i.find('a').get('href') for i in bookurl_list]
        for i in a:
            downurl = ""
            passwd_code = ""
            r = ss.post(i, data=code)
            html = r.text
            soup = BeautifulSoup(html, "html.parser")
            d = soup.find(class_="dltable")
            if d is not None:
                d = d.find('a').get('href')
                c = reString.match(d)
                if c is not None:
                    downurl = c.group(1)
                mm = soup.find(class_="e-secret")
                if mm is not None:
                    passwd_code = mm.get_text()[-4:]
                #print('{0},{1}'.format(downurl, passwd_code))
                if downurl != "" and passwd_code != "":
                    b = [downurl, passwd_code]
                    url_list.append(b)
                    random_second = random.randint(1, 2)
                    time.sleep(1)
        with open(down_list_file, "a") as f:
            for i in url_list:
                f.write(i[0] + "," + i[1] + "\n")
    except Exception as e:
        logger.error(e)
    finally:
        time.sleep(1)
