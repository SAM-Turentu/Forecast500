# -*- coding: utf-8 -*-
# Author: SAM
# Email: SAM-Turentu@outlook.com
# Name: Forecast500
# Filename: FlyweightPattern
# CreateTime: 2021/6/2 21:54
# Summary: '亨元模式'


"""
FlyweightPattern
亨元模式
    特点：运用共享技术有效地支持大量细粒度的对象
"""

import sys


class WebSite:

    def use(self):
        """
        @func name:
        @desc:
        @author: SAM
        @createTime: 2021/6/2 21:56
        @updateTime(upf): 2021/6/2 21:56
        """
        ...


class ConcreteWebSite(WebSite):

    def __init__(self, strName):
        """
        @func name:
        @desc:
        @author: SAM
        @createTime: 2021/6/2 22:16
        @updateTime(upf): 2021/6/2 22:16
        """
        self.name = strName

    def use(self, user):
        """
        @func name:
        @desc:
        @author: SAM
        @createTime: 2021/6/2 22:16
        @updateTime(upf): 2021/6/2 22:16
        """
        print(f'WebSite type: {self.name}, user: {user}')


class UnShareWebSite(WebSite):

    def __init__(self, strName):
        """
        @func name:
        @desc:
        @author: SAM
        @createTime: 2021/6/2 22:17
        @updateTime(upf): 2021/6/2 22:17
        """
        self.name = strName

    def use(self, user):
        """
        @func name:
        @desc:
        @author: SAM
        @createTime: 2021/6/2 22:18
        @updateTime(upf): 2021/6/2 22:18
        """
        print(f'UnShare Website type: {self.name}, user: {user}')


class WebFactory:

    def __init__(self):
        """
        @func name:
        @desc:
        @author: SAM
        @createTime: 2021/6/2 22:19
        @updateTime(upf): 2021/6/2 22:19
        """
        test = ConcreteWebSite('test')
        self.webtype = {'test': test}
        self.count = {'test': 0}

    def GetWeb(self, webtype):
        """
        @func name:
        @desc:
        @author: SAM
        @createTime: 2021/6/2 22:19
        @updateTime(upf): 2021/6/2 22:19
        """
        if webtype not in self.webtype:
            temp = ConcreteWebSite(webtype)
            self.webtype[webtype] = temp
            self.count[webtype] = 1
        else:
            temp = self.webtype[webtype]
            self.count[webtype] = self.count[webtype] + 1
        return temp

    def GetCount(self):
        """
        @func name:
        @desc:
        @author: SAM
        @createTime: 2021/6/2 22:21
        @updateTime(upf): 2021/6/2 22:21
        """
        for key in self.webtype:
            print("111type: %s, count:%d" % (key, sys.getrefcount(self.webtype[key])))
            print(f'type: {key}, count: {self.count[key]}')


if __name__ == '__main__':
    f = WebFactory()
    ws = f.GetWeb('blog')
    ws.use('Lee')
    ws2 = f.GetWeb('show')
    ws2.use('Jack')
    ws3 = f.GetWeb('blog')
    ws3.use('Chen')
    ws4 = UnShareWebSite('TEST')
    ws4.use('Mr.Q')
    print(f.webtype)
    f.GetCount()
