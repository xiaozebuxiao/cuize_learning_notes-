import re
info = """
<dic class="xz"><span id="1">小泽</span></div>
<dic class="xl"><span id="1">小李</span></div>
<dic class="xw"><span id="1">小王</span></div>
<dic class="xb"><span id="1">小白</span></div>
"""

# 创建正则表达式对象预加载
obj = re.compile(r'<dic class=\".*?\"><span id=\".*?\">(?P<name>.*?)</span></div>')

# 提取分组的内容
extract_info = re.findall(obj, info)
print(extract_info)