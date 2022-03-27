# 打开文件
file = open("文档_dome", encoding="utf-8")

while True:
    text = file.readline()
    if text == "":  # 等同于 if not text:
        break
    print(text)

# 关闭文件
file.close()