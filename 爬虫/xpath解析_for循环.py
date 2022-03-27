from lxml import html

etree_file = html.parse("xpath解析.html")
li_a_list = etree_file.xpath("/html/body/ul/li")

# 匹配属性对应的属性值
result1 = etree_file.xpath("/html/body/ul/li/a/@href")
print(result1)

for i in li_a_list:
    result1 = i.xpath("./a/text()")
    print(result1)

    # 匹配属性对应的属性值
    result2 = i.xpath("./a/@href")
    print(result2)
