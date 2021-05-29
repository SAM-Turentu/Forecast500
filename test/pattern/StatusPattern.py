# -*- coding: utf-8 -*-
# Author: SAM
# Email: SAM-Turentu@outlook.com
# Name: Forecast500
# Filename: StatusPattern
# CreateTime: 2021/5/29 17:13
# Summary: '状态模式'


"""
StatusPattern
状态模式
    特点：当一个对象的内在状态改变时允许改变其行为，这个对象看起来像是改变了其类
"""


class State:

    def WriteProgram(self):
        """
        @func name:
        @desc:
        @author: SAM
        @createTime: 2021/5/29 17:15
        @updateTime(upf): 2021/5/29 17:15
        """
        ...


class Work:

    def __init__(self):
        """
        @func name:
        @desc:
        @author: SAM
        @createTime: 2021/5/29 17:17
        @updateTime(upf): 2021/5/29 17:17
        """
        self.hour = 9
        self.current = ForenoonState()

    def SetState(self, temp):
        """
        @func name:
        @desc:
        @author: SAM
        @createTime: 2021/5/29 17:19
        @updateTime(upf): 2021/5/29 17:19
        """
        self.current = temp

    def WriteProgram(self):
        """
        @func name:
        @desc:
        @author: SAM
        @createTime: 2021/5/29 17:19
        @updateTime(upf): 2021/5/29 17:19
        """
        self.current.WriteProgram(self)


class NoonState(State):

    def WriteProgram(self, w):
        """
        @func name:
        @desc:
        @author: SAM
        @createTime: 2021/5/29 17:20
        @updateTime(upf): 2021/5/29 17:20
        """
        print('noon working')
        if (w.hour < 13):
            print('fun.')
        else:
            print('need to rest.')


class ForenoonState(State):

    def WriteProgram(self, w):
        """
        @func name:
        @desc:
        @author: SAM
        @createTime: 2021/5/29 17:21
        @updateTime(upf): 2021/5/29 17:21
        """
        if (w.hour < 12):
            print('morning working')
            print('energetic')
        else:
            w.SetState(NoonState())
            w.WriteProgram()


if __name__ == '__main__':
    mywork = Work()
    mywork.hour = 9
    mywork.WriteProgram()
    mywork.hour = 14
    mywork.WriteProgram()
