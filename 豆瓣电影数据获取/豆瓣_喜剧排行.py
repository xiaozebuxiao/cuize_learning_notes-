import requests

# url准备（”?“以后的参数都可以不要，重新封装参数的时候都会再次传入）
url = "https://movie.douban.com/j/chart/top_list"  # ?type=24&interval_id=100%3A90&action=&start=0&limit=20

# 设置页码
for page in range(0, 500, 20):
    start = page

# 重新封装参数
data = {
    "type": "24",
    "interval_id": "100:90",
    "action": "",
    "start": start,
    "limit": "20"
}

# 修改请求载体身份标识
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.81 Safari/537.36"
}

# 发送get请求，传入参数信息
requ = requests.get(url=url, params=data, headers=headers)

# 接收服务器返回的信息
with open("F:\python学习\爬虫_豆瓣top250电影信息\豆瓣_喜剧排行.txt",
          mode='w', encoding="utf-8") as file:
    file.write(str(requ.json()))
    print("文件创建成功！")

# 关闭请求
requ.close()
