# -*- coding: utf-8 -*-
# Author: SAM
# Email: SAM-Turentu@outlook.com
# Name: Forecast500
# Filename: ChainOfResponsibilityPattern
# CreateTime: 2021/5/31 20:42
# Summary: '职责链模式'


"""
ChainOfResponsibility
职责链模式
    特点：使多个对象都有机会处理请求，从而避免发送者和接收者的耦合关系，将对象连成链并沿着这条链传递请求直到被处理
"""


class Request:

    def __init__(self, tcontent, tnum):
        """
        @func name:
        @desc:
        @author: SAM
        @createTime: 2021/5/31 20:50
        @updateTime(upf): 2021/5/31 20:50
        """
        self.content = tcontent
        self.num = tnum


class Manager:

    def __init__(self, temp):
        """
        @func name:
        @desc:
        @author: SAM
        @createTime: 2021/5/31 20:51
        @updateTime(upf): 2021/5/31 20:51
        """
        self.name = temp

    def SetSuccessor(self, temp):
        """
        @func name:
        @desc:
        @author: SAM
        @createTime: 2021/5/31 20:52
        @updateTime(upf): 2021/5/31 20:52
        """
        self.manager = temp

    def GetRequest(self, req):
        """
        @func name:
        @desc:
        @author: SAM
        @createTime: 2021/5/31 20:52
        @updateTime(upf): 2021/5/31 20:52
        """
        ...


class CommonManager(Manager):

    def GetRequest(self, req):
        """
        @func name:
        @desc:
        @author: SAM
        @createTime: 2021/5/31 20:52
        @updateTime(upf): 2021/5/31 20:52
        """
        if (req.num >= 0 and req.num < 10):
            print(f'{self.name} handled {req.num} request.')
        else:
            self.manager.GetRequest(req)


class MajorDomo(Manager):

    def GetRequest(self, req):
        """
        @func name:
        @desc:
        @author: SAM
        @createTime: 2021/5/31 20:54
        @updateTime(upf): 2021/5/31 20:54
        """
        if req.num >= 10:
            print(f'{self.name} handled {req.num} request.')


if __name__ == '__main__':
    common = CommonManager('Zhang')
    major = MajorDomo('Lee')
    common.SetSuccessor(major)
    req = Request('rest', 33)
    common.GetRequest(req)
    req2 = Request('Salary', 3)
    common.GetRequest(req2)
