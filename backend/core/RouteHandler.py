# -*- coding: utf-8 -*-
# Author: SAM
# Email: SAM-Turentu@outlook.com
# Name: Forecast500
# Filename: RouteHandler
# CreateTime: 2021/4/29 20:02
# Summary: 'handlers 路由装饰器'


class RouteDecorator(object):

    def __init__(self):
        """
        @func name: 路由装饰器
        @desc:
        @author: SAM
        @createTime: 2021/4/29 19:50
        @updateTime(upf): 2021/4/29 19:50
        """
        self.url_list = []

    def get_urls(self):
        """
        @func name: 获取所有urls，在 Application 中调用
        @desc:
        @author: SAM
        @createTime: 2021/4/29 19:51
        @updateTime(upf): 2021/4/29 19:51
        """
        return self.url_list

    def __call__(self, _url, name=None):
        """
        @func name: 类被调用执行
        @desc:
        @author: SAM
        @createTime: 2021/4/29 19:51
        @updateTime(upf): 2021/4/29 19:51
        """

        def _(cls):
            """
            @func name:
            @desc:
            @author: SAM
            @createTime: 2021/4/29 19:52
            @updateTime(upf): 2021/4/29 19:52
            """
            self.url_list.append((_url, cls))
            return cls

        return _


Route = RouteDecorator()
