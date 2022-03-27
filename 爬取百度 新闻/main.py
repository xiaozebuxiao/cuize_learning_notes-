#!/usr/bin/python
# -*-coding:utf-8 -*-

import get
import requests

# headers信息
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/98.0.4758.102 Safari/537.36 "
}

# 构建session类
session = requests.session()

# 主页链接
homepage_url = 'https://news.baidu.com/'

# 调用gain_title获得标题
title = get.gain_title(homepage_url, headers=headers, session=session)


