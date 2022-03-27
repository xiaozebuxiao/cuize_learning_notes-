#! /usr/bin/python
# coding:utf-8

import requests

url = "https://www.baidu.com/"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/98.0.4758.102 Safari/537.36"
}

# 设置代理
proxies = {
    "https": "183.129.244.17:1001"  # "http/https":"ip:端口"
}
requ = requests.get(url, headers=headers, timeout=5, proxies=proxies)
print(requ.text)