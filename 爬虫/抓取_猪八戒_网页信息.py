"""
需求：拿到猪八戒网站saas页面的价格、标题、地址
想要的数据在页面源代码中，因此思路为:
1、拿到页面源代码
2、获取和解析数据
"""

import requests
from lxml import etree

# 获取页面源码
url = "https://xian.zbj.com/search/f/?kw=saas"
page_codes = requests.get(url)
page_codes_text = page_codes.text
# print(page_codes_text)

# 进行xpath解析，获得xpath对象
page_codes_xpath = etree.HTML(page_codes_text)
# print(page_codes_xpath)

# 拿到标题对应的所有的div
title_div_list = page_codes_xpath.xpath('//*[@id="utopia_widget_76"]/a/div/div/p//text()')
price_div_list = page_codes_xpath.xpath('//*[@id="utopia_widget_76"]/a/div/div/span//text()')
for title in title_div_list:
    print(title)
for price in price_div_list:
    print(price)
