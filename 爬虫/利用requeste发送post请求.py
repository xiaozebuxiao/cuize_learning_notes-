import requests

url = "https://y.qq.com/n/ryqq/toplist/4"

return_info = {
"cv": 4747474,
"ct": 24,
format: "json",
"inCharset": "utf-8",
"outCharset":" utf-8",
"notice": 0,
"platform": "yqq.json",
"needNewCode": 1,
"uin": 0,
"g_tk_new_20200303": 5381,
"g_tk": 5381,
"cid": 205360410,
"qq": 0,
"reqtype": 1,
}
resp = requests.post(url, data=return_info)

print(resp.json())
