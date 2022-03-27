#!/usr/bin/python
# -*-coding:utf-8 -*-
import requests
from lxml import etree


class Requ_Class(object):
    """
        执行所有请求任务
    """

    def __init__(self, url, session):
        """
        :param url: 请求的url
        :param headers: 请求的头部信息
        :param session: session对象(外部传入)
        """
        self.url = url
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                          "Chrome/98.0.4758.102 Safari/537.36 "
        }
        self.session = requests.session()

    def requests_action(self):
        """
        1、发出请求获得请求信息
        2、获得
        :return:
        """
        requests_info = self.session.get(self.url, headers=self.headers, timeout=5).text

        # 将请求到的内容加载给etree处理，得到etree对象
        etree_object = etree.HTML(requests_info)




