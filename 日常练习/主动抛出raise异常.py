# 创建输入密码的函数
def input_password():
    password_info = input("请输入密码：")

    # 判断密码长度，>=8 为合法密码
    if len(password_info) >= 8:
        print(password_info)
        return password_info

    # <8 位为非法密码，使用Exceotion创建异常对象
    exc_obj = Exception("密码不符合规范！")
    # 使用raise关键字抛出异常
    raise exc_obj


try:
    input_password()
except Exception as result:
    print(result)
