# 定义列表cards_list用于存储名片字典
cards_list = []


def build_cards():
    """
        新建名片
    """
    # 提示用户输入名片信息
    print("请根据提示输入名片信息！")
    name_str = input("姓名：")
    phone_str = input("电话：")
    qq_str = input("qq：")
    email_str = input("邮箱：")
    # 使用用户输入的信息建立一个名片字典
    cards_dict = {
        "name": name_str,
        "phone": phone_str,
        "qq": qq_str,
        "email": email_str
    }
    # 将名片字典添加到cards_list列表中
    cards_list.append(cards_dict)
    # 提示用户添加成功
    print("%s的名片添加成功！" % name_str)
    print("")


def all_cards():
    """
        显示全部
    """
    # 如果没有名片，提示用户没用名片，并返回
    if len(cards_list) == 0:
        print("还没有名片，请先存入名片信息！")
        #
        return
    # 打印表头
    for table_head in ["姓名", "电话", "qq", "邮箱"]:
        print(table_head, end="\t\t")
    # 换行（我也不知道为啥）
    print("")
    # 打印分割线
    print("=" * 50)
    # 遍历名片列表依次输出字典信息
    for cards_info in cards_list:
        print("%s\t\t%s\t\t%s\t\t%s" % (
            cards_info["name"],
            cards_info["phone"],
            cards_info["qq"],
            cards_info["email"]
        ))


def find_cards():
    """
        1.查询名片
        2.对找到的名片删除
        3.对找到的名片进行修改
    """
    # 提示用户输入要查询名片的姓名
    find_name = input("请输入姓名：")
    # 遍历名片列表，判断有无该姓名对应的名片
    for cards_dict in cards_list:
        # 判断用户输入是否与key对应的值一致
        if find_name == cards_dict["name"]:  # cards_dict["name"]其实是根据key取value
            print("姓名\t\t电话\t\tqq\t\t邮箱")
            print("-" * 50)
            print("%s\t\t%s\t\t%s\t\t%s" % (
                cards_dict["name"],
                cards_dict["phone"],
                cards_dict["qq"],
                cards_dict["email"]
            ))
            print("【1】修改名片  【2】删除名片")
            select_info = input("请选择你要进行的操作:")
            if select_info == "1":

                # 修改名片
                amend_info(cards_dict)
            else:
                # 删除名片
                cards_list.remove(cards_dict)
        break
    # 如果cards_list中没有cards_dict，提示用户没有该名片
    else:
        print("对不起！该名片不存在。")


def amend_info(cards_dict):
    """
    修改名片信息
    :param cards_dict: 查询得到的字典
    """
    cards_dict["name"] = amend_info_optimizing(cards_dict["name"], '姓名:')
    cards_dict["phone"] = amend_info_optimizing(cards_dict["phone"], '电话:')
    cards_dict["qq"] = amend_info_optimizing(cards_dict["qq"], 'qq:')
    cards_dict["email"] = amend_info_optimizing(cards_dict["email"], "邮箱:")


def amend_info_optimizing(old_value, input_info):
    """
    优化修改函数amend_info()
    :param input_info: 用户输入的信息
    :param old_value: 没有修改之前的值
    """

    # 提示用户输入信息
    hint_input = input(input_info)
    # 针对用户的输入信息进行判断，如果用户输入了内容，返回输入的信息
    if len(hint_input) > 0:
        return hint_input
    # 针对用户的输入信息进行判断，如果用户没有输入内容，返回原来的字典里存的值
    else:
        return old_value


