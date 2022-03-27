import cards_tools
# 用户操作
user_action = {
    "1": "新建名片",
    "2": "显示全部",
    "3": "查询名片",
    "0": "退出系统",
}

while True:
    print("-" * 50)
    print(
        "1.", user_action["1"],
        "2.", user_action["2"],
        "3.", user_action["3"],
        "0.", user_action["0"],
    )
    print("-" * 50)
    # 提示用户输入
    hint_str = input("你要选择的操作是:")

    # 用户输入1、2、3对名片进行操作
    if hint_str in ["1", "2", "3"]:
        print("正在>>> ", user_action[hint_str])

        if hint_str == "1":
            cards_tools.build_cards()
        elif hint_str == "2":
            cards_tools.all_cards()
        else:
            cards_tools.find_cards()

    # 用户输入0退出系统
    elif hint_str == "0":
        print("正在 ", user_action[hint_str])
        break

    # 用户输入其他内容提示用户输入错误
    else:
        print("请输入正确的操作序号！")
