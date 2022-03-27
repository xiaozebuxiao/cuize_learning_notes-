#!/usr/bin/python
# -*-coding:utf-8 -*-

import datetime
import time
import urllib.error  # 制定URL，获取网页数据
import urllib.request

import requests
import xlwt  # 进行excel操作
from bs4 import BeautifulSoup  # 网页解析，获取数据

# 收集到的常用Header
my_headers = [
    "Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.153 "
    "Safari/537.36",
    "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:30.0) Gecko/20100101 Firefox/30.0",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_2) AppleWebKit/537.75.14 (KHTML, like Gecko) Version/7.0.3 "
    "Safari/537.75.14",
    "Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.2; Win64; x64; Trident/6.0)",
    'Mozilla/5.0 (Windows; U; Windows NT 5.1; it; rv:1.8.1.11) Gecko/20071127 Firefox/2.0.0.11',
    'Opera/9.25 (Windows NT 5.1; U; en)',
    'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; .NET CLR 1.1.4322; .NET CLR 2.0.50727)',
    'Mozilla/5.0 (compatible; Konqueror/3.5; Linux) KHTML/3.5.5 (like Gecko) (Kubuntu)',
    'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.8.0.12) Gecko/20070731 Ubuntu/dapper-security Firefox/1.5.0.12',
    'Lynx/2.8.5rel.1 libwww-FM/2.14 SSL-MM/1.4.1 GNUTLS/1.2.9',
    "Mozilla/5.0 (X11; Linux i686) AppleWebKit/535.7 (KHTML, like Gecko) Ubuntu/11.04 Chromium/16.0.912.77 "
    "Chrome/16.0.912.77 Safari/535.7",
    "Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:10.0) Gecko/20100101 Firefox/10.0 "
]


def main():
    url = "http://www.people.com.cn/"  # 要爬取的网页链接
    url2 = "http://politics.people.com.cn/n1/2021/1101/c1024-32269623.html"
    # 1.爬取网页
    datalist = getData(url)
    # print(getDataContext(url2))
    savepath = "人民网_" + str(datetime.date.today()) + ".xls"  # 当前目录新建XLS，存储进去
    # 3.保存数据
    saveData(datalist, savepath)  # 2种存储方式可以只选择一种


# 爬取网页
def getData(url):
    datalist = []  # 用来存储爬取的网页信息
    html = askURL(url)  # 保存获取到的网页源码
    i = 0
    # 2.逐一解析数据
    soup = BeautifulSoup(html, "html.parser")
    for item in soup.find_all('a'):  # 查找符合要求的字符串
        data = []  # 保存一条链接所有信息
        if item.get('href') is not None and item.get_text() is not None and str(
                datetime.datetime.now().year) + "/" + str(datetime.datetime.now().month) in item.get(
                'href') and "http" in item.get('href'):
            time.sleep(3)
            title = item.get_text()
            newsurl = item.get('href')
            data.append(title)  # 列1：标题
            data.append(newsurl)  # 列2：url
            datacontext = getDataContext(newsurl)  # 目前这里有问题，403 Forbidden
            # datacontext = None
            if datacontext is not None and len(datacontext) == 3:
                data.append(datacontext[0])  # 列3：分类频道
                data.append(datacontext[1])  # 列4：发文时间
                data.append(datacontext[2])  # 列5：正文
            else:
                data.append(0)  # 列3：分类频道
                data.append(0)  # 列4：发文时间
                data.append(0)  # 列5：正文
            data.append(str(datetime.datetime.now()))  # 列6：爬取时间
            datalist.append(data)
            print("!!!i:" + str(i) + "!!!data" + str(data))
            i += 1
            time.sleep(1)
            if i >= 30:
                break
    return datalist


# 爬取正文
def getDataContext(url):
    print(url)
    head = {  # 模拟浏览器头部信息，向豆瓣服务器发送消息
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36 Edg/95.0.1020.30"
    }
    # 用户代理，表示告诉服务器，我们是什么类型的机器、浏览器（本质上是告诉浏览器，我们可以接收什么水平的文件内容）

    html = requests.get(url, headers=head)
    html.encoding = 'gbk'
    soup = BeautifulSoup(html.text, 'html.parser')

    data = []  # 保存一条链接所有信息
    channel = ""
    pubtime = ""
    context = ""
    # 2.逐一解析数据
    for item in soup.find_all('div', id='rwb_navpath'):  # 查找符合要求的字符串
        channel += item.get_text()
        time.sleep(1)
    for item in soup.find_all('div', class_="col-1-1"):  # 查找符合要求的字符串
        pubtime += item.get_text().strip()
        time.sleep(1)
    for item in soup.find_all('div', class_="rm_txt_con cf"):  # 查找符合要求的字符串
        context += item.get_text()
        time.sleep(1)
    print(channel)
    print(pubtime)
    print(context)
    data.append(channel)
    data.append(pubtime)
    data.append(context)

    return data


# 得到指定一个URL的网页内容
def askURL(url):
    head = {  # 模拟浏览器头部信息，向豆瓣服务器发送消息
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36 Edg/95.0.1020.30"
    }
    # 用户代理，表示告诉服务器，我们是什么类型的机器、浏览器（本质上是告诉浏览器，我们可以接收什么水平的文件内容）

    request = urllib.request.Request(url, headers=head)
    html = ""
    try:
        response = urllib.request.urlopen(request)
        html = response.read().decode("gbk")
    except urllib.error.URLError as e:
        if hasattr(e, "code"):
            print(e.code)
        if hasattr(e, "reason"):
            print(e.reason)
    return html


# 换一个方法get网页内容
def askGetURL(url):
    head = {  # 模拟浏览器头部信息，向豆瓣服务器发送消息
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36 Edg/95.0.1020.30"
    }
    # 用户代理，表示告诉服务器，我们是什么类型的机器、浏览器（本质上是告诉浏览器，我们可以接收什么水平的文件内容）

    res = requests.get(url, headers=head).content.decode("gbk")
    return res


# 保存数据到表格
def saveData(datalist, savepath):
    print("save.......")
    book = xlwt.Workbook(encoding="utf-8", style_compression=0)  # 创建workbook对象
    sheet = book.add_sheet('人民网_' + str(datetime.date.today()), cell_overwrite_ok=True)  # 创建工作表
    col = ("新闻标题", "新闻链接", "分类频道", "发文时间", "正文", "爬取时间")
    for i in range(0, 6):
        sheet.write(0, i, col[i])  # 列名
    k = 0
    for data in datalist:
        # print("第%d条" %(k+1))       #输出语句，用来测试
        for j in range(0, 6):
            sheet.write(k + 1, j, data[j])  # 数据
            # print(data[j])       #输出语句，用来测试
        k += 1
    book.save(savepath)  # 保存


if __name__ == "__main__":  # 当程序执行时
    # 调用函数
    main()
    print("爬取完毕！")
