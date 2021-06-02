# -*- coding: utf-8 -*-
# Author: SAM
# Email: SAM-Turentu@outlook.com
# Name: Forecast500
# Filename: CommandPattern
# CreateTime: 2021/5/31 20:05
# Summary: '命令模式'


"""
CommandPattern
命令模式
    特点：将请求封装成对象，从而使可用不听的请求对客户进行参数化；对请求排队或记录请求日志，以及支持可撤销的操作
"""


class Barbucer:

    def MakeMutton(self):
        """
        @func name:
        @desc:
        @author: SAM
        @createTime: 2021/5/31 20:08
        @updateTime(upf): 2021/5/31 20:08
        """
        print('Mutton')

    def MakeChickenWing(self):
        """
        @func name:
        @desc:
        @author: SAM
        @createTime: 2021/5/31 20:08
        @updateTime(upf): 2021/5/31 20:08
        """
        print('Chicken Wing')


class Command:

    def __init__(self, temp):
        """
        @func name:
        @desc:
        @author: SAM
        @createTime: 2021/5/31 20:09
        @updateTime(upf): 2021/5/31 20:09
        """
        self.receiver = temp

    def ExecuteCmd(self):
        """
        @func name:
        @desc:
        @author: SAM
        @createTime: 2021/5/31 20:09
        @updateTime(upf): 2021/5/31 20:09
        """
        ...


class BakeMuttonCmd(Command):

    def ExecuteCmd(self):
        """
        @func name:
        @desc:
        @author: SAM
        @createTime: 2021/5/31 20:09
        @updateTime(upf): 2021/5/31 20:09
        """
        self.receiver.MakeMutton()


class ChickenWingCmd(Command):

    def ExecuteCmd(self):
        """
        @func name:
        @desc:
        @author: SAM
        @createTime: 2021/5/31 20:10
        @updateTime(upf): 2021/5/31 20:10
        """
        self.receiver.MakeChickenWing()


class Waiter:
    def __init__(self):
        """
        @func name:
        @desc:
        @author: SAM
        @createTime: 2021/5/31 20:10
        @updateTime(upf): 2021/5/31 20:10
        """
        self.order = []

    def SetCmd(self, command):
        """
        @func name:
        @desc:
        @author: SAM
        @createTime: 2021/5/31 20:11
        @updateTime(upf): 2021/5/31 20:11
        """
        self.order.append(command)
        print('Add Order')

    def Notify(self):
        """
        @func name:
        @desc:
        @author: SAM
        @createTime: 2021/5/31 20:11
        @updateTime(upf): 2021/5/31 20:11
        """
        for cmd in self.order:
            cmd.ExecuteCmd()


if __name__ == '__main__':
    barbucer = Barbucer()
    cmd = BakeMuttonCmd(barbucer)
    cmd2 = ChickenWingCmd(barbucer)
    girl = Waiter()
    girl.SetCmd(cmd)
    girl.SetCmd(cmd2)
    girl.Notify()
