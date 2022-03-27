# *-* coding:utf8 *-*
# 打开文件
old_file = open("文档操作/文档_dome", encoding="utf-8")
new_file = open("文档操作/文档_dome(复件)", "w", encoding="utf-8")

# 读、写文件
while True:
    read_file = old_file.readline()
    # 判断是否读取到内容
    if read_file == "":
        break
    # 将读取到的内容写入new_file
    new_file.write(read_file)

# 关闭文件
old_file.close()
new_file.close()
