#!/usr/bin/python
# -*-coding:utf-8 -*-


import asyncio, aiohttp, os

urls = [
    "http://kr.shanghai-jiuxin.com/file/2022/0225/b355023157449f9f93c8b8bad830206e.jpg"
    "http://kr.shanghai-jiuxin.com/file/2022/0225/994df900b87237a47d7dcf0bfe6c27f0.jpg"
    "http://kr.shanghai-jiuxin.com/file/2022/0225/98638eea610a50e6bd3708c0e9322bc5.jpg"
]


async def aiodownload(url):
    # 发送请求
    # 得到图片内容
    # 保存图片
    name = url.rsplit("/", -1)[-1]  # 从右切割，得到[-1]位置的内容
    # 新建会话（类似于引入requsts模块）
    async with aiohttp.ClientSession() as session:  # with --> 上下文管理器
        async with session.get(url) as resp:
            # 将请求回来的数据写入文件
            with open(name, mode='wb') as f:    # 创建文件
                f.write(await resp.content.read())  # 读取内容是异步的，需要await挂起
        # session.post()
    print("%s下载成功！" % name)


async def main():
    tasks = []
    for url in urls:
        tasks.append(aiodownload(url))

    # 运行任务列表
    await asyncio.create_task(tasks)


if __name__ == '__main__':
    asyncio.run(main())