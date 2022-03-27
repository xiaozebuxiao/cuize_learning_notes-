import re

# result = re.finditer(r"\d+", "今天我用100元，买了2只鸡。")
# for iter in result:
#     # 迭代器返回的是一个match对象，通过group方法就可以提取到值
#     iter_match = iter.group()
#     print(iter_match)


# 提前准备一个正则表达式
obj = re.compile(r"\d+")

# 需要的时候通过re.findall（）、re.search（）、re.finditer（）调用
result = obj.findall("今天我用100元，买了2只鸡。")
print(result)
