#!/usr/bin/python
# -*-coding:utf-8 -*-
import requests
from lxml import etree
import time


# 获取title
def gain_title(homepage_url, headers, session):
    # 请求主页链接
    homepage_sound_code_text = session.get(homepage_url, headers=headers, timeout=5).text
    # print(homepage_sound_code_text)

    # 将在线文档加载给etree处理
    ul = etree.HTML(homepage_sound_code_text)

    # 提取标题
    title_list = ul.xpath('//*[@id="pane-news"]/ul/li/a/text()')

    # 提取详情页url
    son_url_list = ul.xpath('//*[@id="pane-news"]/ul/li/a/@href')

    with open('F:/python学习/百度新闻_整个页面/nows_info.txt', mode='a+', encoding="utf-8") as t:
        for (title, son_url) in zip(title_list, son_url_list):
            t.write(title + '\t' + son_url + '\n')
