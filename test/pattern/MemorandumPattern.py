# -*- coding: utf-8 -*-
# Author: SAM
# Email: SAM-Turentu@outlook.com
# Name: Forecast500
# Filename: MemorandumPattern
# CreateTime: 2021/5/29 18:54
# Summary: '备忘录模式'


"""
MemorandumPattern
备忘录模式
    特点：在不破坏封装性的前提下捕获一个对象的内部状态，并在该对象之外保存这个状态，以后可以将对象恢复到这个状态
"""


class Originator:

    def __init__(self):
        """
        @func name:
        @desc:
        @author: SAM
        @createTime: 2021/5/29 18:59
        @updateTime(upf): 2021/5/29 18:59
        """
        self.state = ''

    def Show(self):
        """
        @func name:
        @desc:
        @author: SAM
        @createTime: 2021/5/29 18:59
        @updateTime(upf): 2021/5/29 18:59
        """
        print(self.state)

    def CreateMemo(self):
        """
        @func name:
        @desc:
        @author: SAM
        @createTime: 2021/5/29 19:00
        @updateTime(upf): 2021/5/29 19:00
        """
        return Memo(self.state)

    def SetMemo(self, memo):
        """
        @func name:
        @desc:
        @author: SAM
        @createTime: 2021/5/29 19:00
        @updateTime(upf): 2021/5/29 19:00
        """
        self.state = memo.state


class Memo:
    state = ''

    def __init__(self, ts):
        """
        @func name:
        @desc:
        @author: SAM
        @createTime: 2021/5/29 19:01
        @updateTime(upf): 2021/5/29 19:01
        """
        self.state = ts


class Caretaker:
    memo = ''


if __name__ == '__main__':
    on = Originator()
    on.state = 'on'
    on.Show()
    c = Caretaker()
    c.memo = on.CreateMemo()
    on.state = 'off'
    on.Show()
    on.SetMemo(c.memo)
    on.Show()
