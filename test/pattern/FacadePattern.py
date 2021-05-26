# -*- coding: utf-8 -*-
# Author: SAM
# Email: SAM-Turentu@outlook.com
# Name: Forecast500
# Filename: FacadePattern
# CreateTime: 2021/5/26 14:29
# Summary: '外观模式'

"""
FacadePattern
外观模式
    特点：为一组调用提供一致的接口
"""


class SubSystemOne:

    def MethodOne(self):
        """
        @author: SAM
        @CreateTime: 2021/5/26 14:31
        @UpdateTime(upf): 2021/5/26 14:31
        @desc: ''
        """
        print('SubSysOne')


class SubSystemTwo:

    def MethodTwo(self):
        """
        @author: SAM
        @CreateTime: 2021/5/26 14:32
        @UpdateTime(upf): 2021/5/26 14:32
        @desc: ''
        """
        print('SubSysTwo')


class SubSystemThree:

    def MethodThree(self):
        """
        @author: SAM
        @CreateTime: 2021/5/26 14:32
        @UpdateTime(upf): 2021/5/26 14:32
        @desc: ''
        """
        print('SubSysThree')


class SubSystemFour:

    def MehtodFour(self):
        """
        @author: SAM
        @CreateTime: 2021/5/26 14:33
        @UpdateTime(upf): 2021/5/26 14:33
        @desc: ''
        """
        print('SubSysFour')


class Facade:

    def __init__(self):
        """
        @author: SAM
        @CreateTime: 2021/5/26 14:33
        @UpdateTime(upf): 2021/5/26 14:33
        @desc: ''
        """
        self.one = SubSystemOne()
        self.two = SubSystemTwo()
        self.three = SubSystemThree()
        self.four = SubSystemFour()

    def MethodA(self):
        """
        @author: SAM
        @CreateTime: 2021/5/26 14:34
        @UpdateTime(upf): 2021/5/26 14:34
        @desc: ''
        """
        print('MethodA')
        self.one.MethodOne()
        self.two.MethodTwo()
        self.four.MehtodFour()

    def MethodB(self):
        """
        @author: SAM
        @CreateTime: 2021/5/26 14:35
        @UpdateTime(upf): 2021/5/26 14:35
        @desc: ''
        """
        print('MethodB')
        self.two.MethodTwo()
        self.three.MethodThree()


if __name__ == '__main__':
    facad = Facade()
    facad.MethodA()
    facad.MethodB()
