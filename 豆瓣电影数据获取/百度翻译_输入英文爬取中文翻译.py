import requests

# 准备一个目标url
url = "https://fanyi.baidu.com/sug"

# 准备请求信息
requ_info = input("请输入你要查询的单词：")

# 将请求信息放在字典中进行存储
requ_info_dict = {"kw": requ_info}

# 通过data参数传递请求信息，发送post请求

requ = requests.post(url, requ_info_dict)

# 接收服务器返回内容
print(requ.json())