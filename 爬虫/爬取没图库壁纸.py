import requests
from bs4 import BeautifulSoup
import os
import re
import time

last_page = int(input("请输入不要爬的页数："))
for i in range(1, last_page+1):
    if i == 1:
        # 主页地址
        url = "https://www.53pic.com/bizhi/dongman/"
        # print(url)
    else:
        url = "https://www.53pic.com/bizhi/dongman/index_%s.html" % str(i)
        # url.replace("2", str(i))
        # print(url)
        i += 1

# url = "https://www.53pic.com/bizhi/dongman/index_3.html"
# -----------------1、拿到主页面源代码，找到href提取子链接----------------------
gain_home = requests.get(url)
# 处理解析后的乱码
gain_home.encoding = "utf-8"
# print(gain_home.text)

# -------2、通过herf拿到子页面内容，从子页面中找到图片下载地址   <img src=”“>------

son_link = BeautifulSoup(gain_home.text, "html.parser")
son_link_list = son_link.find_all(name="a", attrs={"class": "title-content"})
for a in son_link_list:
    # print(son_link_list)  测试代码
    # ---------------------------------3、下载图片------------------------------
    # 获取到子页面链接
    son_link = "https://www.53pic.com" + a.get("href")
    # print(son_link)
    # 从子页面中拿到页面源代码
    son_code = requests.get(son_link)
    # 处理解析后的乱码
    son_code.encoding = "utf-8"
    son_code_text = son_code.text
    # print(son_code_text)
    wallpaper_link = BeautifulSoup(son_code_text, features="html.parser")
    ing_url_info = wallpaper_link.find(name="div", attrs={"id": "showimgXFL", "class": "cl mbv"})
    ing_url = ing_url_info.find("img")
    img = ing_url.get("src")  # 获取src属性值
    print(img)
    bz = requests.get(img)
    name = img.split("/")[-1]
    os.chdir(r"C:\Users\崔泽\Desktop\mig")
with open(name, mode='wb+') as file:
    file.write(bz.content)
    time.sleep(1)
# a = os.getcwd()
# print(a)
print("%s下载成功！" % img)
