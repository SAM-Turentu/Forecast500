# -*- coding: utf-8 -*-
# Author: SAM
# Email: SAM-Turentu@outlook.com
# Name: Forecast500
# Filename: BridgePattern
# CreateTime: 2021/5/31 19:52
# Summary: '桥接模式'


"""
BridgePattern
桥接模式
    特点：将抽象部分与它的实现部分分离，使它们可以独立地变化
"""


class HandsetSoft(object):

    def Run(self):
        """
        @func name:
        @desc:
        @author: SAM
        @createTime: 2021/5/31 19:53
        @updateTime(upf): 2021/5/31 19:53
        """
        ...


class HandsetGame(HandsetSoft):

    def Run(self):
        """
        @func name:
        @desc:
        @author: SAM
        @createTime: 2021/5/31 19:54
        @updateTime(upf): 2021/5/31 19:54
        """
        print('Game')


class HandsetAddressList(HandsetSoft):

    def Run(self):
        """
        @func name:
        @desc:
        @author: SAM
        @createTime: 2021/5/31 19:55
        @updateTime(upf): 2021/5/31 19:55
        """
        print('Address List')


class HandsetBrand(object):

    def __init__(self):
        """
        @func name:
        @desc:
        @author: SAM
        @createTime: 2021/5/31 19:55
        @updateTime(upf): 2021/5/31 19:55
        """
        self.m_soft = None

    def SetHandsetSoft(self, temp):
        """
        @func name:
        @desc:
        @author: SAM
        @createTime: 2021/5/31 19:56
        @updateTime(upf): 2021/5/31 19:56
        """
        self.m_soft = temp

    def Run(self):
        """
        @func name:
        @desc:
        @author: SAM
        @createTime: 2021/5/31 19:56
        @updateTime(upf): 2021/5/31 19:56
        """
        ...


class HandsetBrandM(HandsetBrand):

    def Run(self):
        """
        @func name:
        @desc:
        @author: SAM
        @createTime: 2021/5/31 19:56
        @updateTime(upf): 2021/5/31 19:56
        """
        if not (self.m_soft == None):
            print('BrandM')
            self.m_soft.Run()


class HandsetBrandN(HandsetBrand):

    def Run(self):
        """
        @func name:
        @desc:
        @author: SAM
        @createTime: 2021/5/31 19:58
        @updateTime(upf): 2021/5/31 19:58
        """
        if not (self.m_soft == None):
            print('BrandN')
            self.m_soft.Run()


if __name__ == '__main__':
    brand = HandsetBrandM()
    brand.SetHandsetSoft(HandsetGame())
    brand.Run()
    brand.SetHandsetSoft(HandsetAddressList())
    brand.Run()
