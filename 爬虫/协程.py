#!/usr/bin/python
# -*-coding:utf-8 -*-


import asyncio  # 要想使用协程，必须导入asyncio模块
# import time


# 创建任务一
async def func1():  # 构建异步函数
    await asyncio.sleep(3)
    print("异步线程01")


# 创建任务二
async def func2():
    await asyncio.sleep(2)
    print("异步线程02")


# 创建任务三
async def func3():
    await asyncio.sleep(4)
    print("异步线程03")


async def main():
    # 创建协程任务(协程对象)
    tasks = [
        # 版本原因，需要通过asyncio.create_task()函数调用协程函数，创建协程对象
        asyncio.create_task(func1()),
        asyncio.create_task(func2()),
        asyncio.create_task(func3())
    ]

    # 挂载协程对象
    await asyncio.wait(tasks)


if __name__ == '__main__':
    # 通过传入main函数对象，执行协程对象
    asyncio.run(main())