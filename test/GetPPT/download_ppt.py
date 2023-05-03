# -*- coding: utf-8 -*-
# Author: SAM
# Email: SAM-Turentu@outlook.com
# Name: Forecast500
# Filename: download_ppt
# CreateTime: 2022/7/6 19:33
# Summary: ''


import requests
from lxml import etree


class Downlaods(object):

    def __init__(self):
        self.base_url = 'https://www.2ppt.com/'

    def get_response(self, url):
        """
        @func name:
        @desc:
        @author: SAM
        @createTime: 2022/7/6 19:35
        @updateTime(upf): 2022/7/6 19:35
        """
        headers = {}
        response = requests.get(url, headers=headers, timeout=10)
        self.text = response.text

    def parse_response(self):
        """
        @func name:
        @desc:
        @author: SAM
        @createTime: 2022/7/6 19:37
        @updateTime(upf): 2022/7/6 19:37
        """
        html = etree.HTML(self.text)








