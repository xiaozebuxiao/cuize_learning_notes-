#!/usr/bin/python
# -*-coding:utf-8 -*-

import requests
from lxml import etree


def download_homepage_source_code(url):
    # 获取主页源代码
    requ_homepage_source_code = requests.get(url)
    requ_homepage_source_code.encoding = "utf-8"
    # print(requ_homepage_source_code.text)
    html = etree.HTML(requ_homepage_source_code.text)
    table = html.xpath('//*[@id="bbs"]/div/div/div/div[4]/div[1]/div/table')[0]
    trs = table.xpath('./tr')
    print(len(table))

    # for tr in table:
    #     txt = tr.xpath('//*[@id="bbs"]/div/div/div/div[4]/div[1]/div/table/tr/td')[0]
    #     print(txt)


if __name__ == '__main__':
    download_homepage_source_code("http://www.xinfadi.com.cn/priceDetail.html")
