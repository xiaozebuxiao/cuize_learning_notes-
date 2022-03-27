import requests

# 记录信息
kdj_info = {"cname": "",
            "pid": "",
            "keyword": "西安",
            "pageIndex": 2,
            "pageSize": 10
            }

# 发送请求
req_info = requests.post("http://www.kfc.com.cn/kfccda/ashx/GetStoreList.ashx?op=keyword", kdj_info)
req_info.encoding = "utf-8"
with open("肯德基.text", mode="w", encoding="utf-8") as result:
    result.write(req_info.text)
