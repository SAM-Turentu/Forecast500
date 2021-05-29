# -*- coding: utf-8 -*-
# Author: SAM
# Email: SAM-Turentu@outlook.com
# Name: Forecast500
# Filename: AdapterPattern
# CreateTime: 2021/5/29 17:31
# Summary: '适配器模式'


"""
AdapterPattern
适配器模式
    特点：将一个类的接口转换成为客户希望的另一个接口
"""


class Target:

    def Request(self):
        """
        @func name:
        @desc:
        @author: SAM
        @createTime: 2021/5/29 17:32
        @updateTime(upf): 2021/5/29 17:32
        """
        print('common request.')


class Adaptee(Target):

    def SpecificRequest(self):
        """
        @func name:
        @desc:
        @author: SAM
        @createTime: 2021/5/29 17:33
        @updateTime(upf): 2021/5/29 17:33
        """
        print('specific request.')


class Adapter(Target):

    def __init__(self, ada):
        """
        @func name:
        @desc:
        @author: SAM
        @createTime: 2021/5/29 17:33
        @updateTime(upf): 2021/5/29 17:33
        """
        self.adaptee = ada

    def Request(self):
        """
        @func name:
        @desc:
        @author: SAM
        @createTime: 2021/5/29 17:34
        @updateTime(upf): 2021/5/29 17:34
        """
        self.adaptee.SpecificRequest()


if __name__ == '__main__':
    adaptee = Adaptee()
    adapter = Adapter(adaptee)
    adapter.Request()
