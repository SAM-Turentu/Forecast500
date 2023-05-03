# -*- coding: utf-8 -*-
# Author: SAM
# Email: SAM-Turentu@outlook.com
# Name: Forecast500
# Filename: http_request
# CreateTime: 2022/7/6 20:23
# Summary: ''


import requests


class HttpRequest(object):

    def __init__(self, url=None, headers=None, *args, **kwargs):
        self.url = url
        self.headers = headers

    # def __getattribute__(self, item):
    #     return super(HttpRequest, self).__getattribute__(item)
    #     # return getattr(self, item)
    #
    # def __setattr__(self, key, value):
    #     super(HttpRequest, self).__setattr__(key, value)

    def get_reponse(self, url: list or str = None):
        """
        @func name:
        @desc:
        @author: SAM
        @createTime: 2022/7/6 20:24
        @updateTime(upf): 2022/7/6 20:24
        """
        url = url if not self.url else self.url
        if type(url) == list:
            ...
        params = None
        response = requests.get(url, headers=self.headers, params=params, timeout=15)
        return response
