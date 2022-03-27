import requests

url = "https://www.baidu.com/"

# 发送请求
resp = requests.get(url)
# 设置编码格式
resp.encoding = "utf-8"
# 将数据返回到一个文件
with open("mybaidu.html", mode='w', encoding="utf-8") as file:
    file.write(resp.text)