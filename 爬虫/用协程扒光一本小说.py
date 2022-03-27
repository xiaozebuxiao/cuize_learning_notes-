#!/usr/bin/python
# -*-coding:utf-8 -*-
import asyncio
import requests

"""
1、同步操作：访问getCatalog拿到所有章节的cid和名称
2、异步操作：访问getChaptent下载所有文章内容
"""


async def aiodownload(cid, b_id, title):
    pass


def getCatalog(url):
    # 同步操作
    for i in range(1, 4):
        head = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                          "Chrome/98.0.4758.102 Safari/537.36 "
        }
        section_url = 'https://zboxnovel.baidu.com/boxnovel/detail?gid=4306063500&data=%7B%22fromaction%22%3A%22dushu' \
                      '%22%7D '
        # print(section_url)
        requ = requests.get(section_url, headers=head, timeout=5)
        # print(requ.text)

        dic = requ.json()
        tasks = []
        for item in dic.get('data', {}).get('chapter', {}).get('chapterInfo', {}).get('chapter_title'):
            chapter_title = item['chapter_title']
            book_id = item['book_id']
            # tasks.append(aiodownload(cid, b_id, title))
            print(chapter_title, book_id)

        # await asyncio.wait(cid, b_id, title)


if __name__ == '__main__':
    url = 'www.baidu.com'
    getCatalog(url)
