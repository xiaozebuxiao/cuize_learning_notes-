#!/usr/bin/python
# -*-coding:utf-8 -*-
import requests, asyncio, aiohttp


for i in range(1, 4):
    head = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                      "Chrome/98.0.4758.102 Safari/537.36 "
    }
    section_url = 'https://boxnovel.baidu.com/boxnovel/detail?gid=4306063500&data=%7B%22fromaction%22%3A%22dushu%22%7D'

    # print(section_url)
    requ = requests.get(section_url, headers=head, timeout=5)
    print(requ.text)

