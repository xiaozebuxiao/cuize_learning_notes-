import re

data = """
<div>
    <div><a href="baidu.com">我是百度</a></div>
    <div><a href="qq.com">我是网易</a></div>
    <div><a href="163.com">我是网易</a></div>
    <div><a href="wane">我是美图</a></div>
</div>
"""
obj1 = re.compile(r'<div><a href=".*?">.*?</a></div>')
# 匹配""内的内容和><之间的内容，并通过?P<>对匹配的内容分组
obj = re.compile(r'<div><a href="(?P<url>.*?)">(?P<txt>.*?)</a></div>')

for info in obj.finditer(data):
    url = info.group("url")
    txt = info.group("txt")
    print(url, txt)

    # 利用groupdict将匹配内容通过一个字典输出
    # print(info.groupdict())
