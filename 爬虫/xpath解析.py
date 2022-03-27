from lxml import html


# 通过html模块使用原来etree模块的功能
etree_file = html.parse("xpath解析.html")

# 通过节点匹配对应的内容
# extract_html = etree_file.xpath("/html/body/ul/li/a/text()")    # text()就可以拿到对应节点的文字
#
# 当有多个相同节点时可通过[索引]进行提取（比较特殊，从1开始数）
# extract_html = etree_file.xpath("/html/body/ul/li[2]/a/text()")

# 通过[@属性=属性值]匹配对应的内容
extract_html = etree_file.xpath("/html/body/ol/li/a[@href='dapao']/text()")

print(extract_html)
