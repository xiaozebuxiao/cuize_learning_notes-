import requests

# 新建session会话
session = requests.session()

data = {
    "loginName": "18146864450",
    "password": "Cuize88888888"
}

url = "https://user.17k.com/www/bookshelf/index.html"

resp = session.post(url, data=data)
resp.encoding = "utf-8"
print(resp.text)
print(resp.cookies)
