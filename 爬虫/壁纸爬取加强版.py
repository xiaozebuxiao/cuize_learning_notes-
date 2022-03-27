import os
import time
import requests
from bs4 import BeautifulSoup

# 需要爬取的页数
gain_page = int(input("请输入你需要爬取的页数："))
# 根据页数进行逻辑判断
for i in range(1, gain_page + 1):
    if i == 1:
        url = "https://www.53pic.com/bizhi/dongman/"
    else:
        url = "https://www.53pic.com/bizhi/dongman/index_%s.html" % str(i)

    # print(url)    # 测试代码

    # ---------------提取主页源代码--------------- #
    # 向服务器请求数据
    main_page_info = requests.get(url)
    # 解决乱码问题
    main_page_info.encoding = "utf-8"
    main_page_text = main_page_info.text
    # print(main_page_text)

    # -------2、通过href拿到子页面内容，从子页面中找到图片下载地址   <img src=”“>------

    # 将主页源码交给BeautifulSoup处理
    handle_main = BeautifulSoup(main_page_text, "html.parser")
    # print(handle_main)
    # 缩小数据匹配范围
    son_link_list_a = handle_main.find_all(name="a", attrs={"class": "title-content"})
    # print(son_link_list)

    # 通过循环取出a标签中的href、标题
    for a_href_a in son_link_list_a:
        # print(a_href_a)
        href = "https://www.53pic.com" + a_href_a.get("href")
        title = a_href_a.get("title")
        # print(href, title)

        # 拿到子页面的页面源代码
        son_page_info = requests.get(href)
        # 解决中文乱码问题
        son_page_info.encoding = "utf-8"
        son_page_info_text = son_page_info.text
        # print(son_page_info_text)
        # 将子页面交给BeautifulSoup处理
        handle_son = BeautifulSoup(son_page_info_text, "html.parser")
        # 缩小子页面数据匹配范围
        download_link_p = handle_son.find_all(name="div", attrs={"id": "showimgXFL"})
        # print(download_link_p)
        for div_src_div in download_link_p:
            # print(div_src_div)
            # 查找img标签
            download_src_img = div_src_div.find("img")
            # 匹配src属性
            download_src = download_src_img.get("src")
            # 请求下载
            download = requests.get(download_src)
            # print(download_src)
            # 切换工作目录
            os.chdir(r"C:\Users\崔泽\Desktop\mig")
            with open("%s.jpg" % title, mode='wb+') as file:
                # 以二进制文件写入文件
                file.write(download.content)
                time.sleep(1)
            print("%s...下载成功！" % title)
