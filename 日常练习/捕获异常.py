try:
    # 尝试执行代码
    pass
except 错误类型1:
    # 针对错误类型1,对应的代码处理
    pass
except (错误类型2, 错误类型3):
    # 针对针对错误类型2和3,对应的代码处理
    pass
except Exception as 变量名:
    # 针对其他未知错误,进行的代码处理
    pass
else:
    # 没有异常执行的代码
    pass
finally:
    # 无论是否有异常，都会执行的代码
    pass