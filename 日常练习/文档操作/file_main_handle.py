# 打开文件，返回文件操作对象
file = open("文档_dome", "r", encoding='utf-8')  # 参数为r时，执行读取文件

# 追加内容
# text = file.write("追加内容。。。")

# 读取文件内容
text_r = file.read()
print(text_r)

print(type(text_r))

# 关闭文件
file.close()
