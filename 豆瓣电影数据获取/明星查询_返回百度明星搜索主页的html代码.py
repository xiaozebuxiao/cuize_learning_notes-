import requests

# 准备查询信息
info = input("请输入你要查询的明星：")
# 1、为爬虫请求准备一个url
url = f'https://www.sogou.com/web?query={info}'

# 此处服务器检查到程序是由程序发起的，需要做一个请求身份处理
dic = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:96.0) Gecko/20100101 Firefox/96.0"}

# 2、请求服务器
resp = requests.get(url, headers=dic)

# 3、接收返回内容
print(resp.text)
