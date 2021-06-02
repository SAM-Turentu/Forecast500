# -*- coding: utf-8 -*-
# Author: SAM
# Email: SAM-Turentu@outlook.com
# Name: Forecast500
# Filename: MediatorPattern
# CreateTime: 2021/6/2 19:03
# Summary: '中介者模式'


"""
MediatorPattern
中介者模式
    特点：用一个对象来封装一系列的对象交互，中介者使各对象不需要显示地互相引用，从而使耦合松散，而且可以独立地改变它们之间的交互
"""


class Mediator:

    def send(self, message, col):
        """
        @func name:
        @desc:
        @author: SAM
        @createTime: 2021/6/2 20:18
        @updateTime(upf): 2021/6/2 20:18
        """
        ...


class Colleague:

    def __init__(self, temp):
        """
        @func name:
        @desc:
        @author: SAM
        @createTime: 2021/6/2 20:21
        @updateTime(upf): 2021/6/2 20:21
        """
        self.mediator = temp


class Colleague1(Colleague):

    def send(self, message):
        """
        @func name:
        @desc:
        @author: SAM
        @createTime: 2021/6/2 20:22
        @updateTime(upf): 2021/6/2 20:22
        """
        self.mediator.send(message, self)

    def notify(self, message):
        """
        @func name:
        @desc:
        @author: SAM
        @createTime: 2021/6/2 20:21
        @updateTime(upf): 2021/6/2 20:21
        """
        print('Colleague1 get a message: ', message)


class Colleague2(Colleague):

    def send(self, message, col):
        """
        @func name:
        @desc:
        @author: SAM
        @createTime: 2021/6/2 20:24
        @updateTime(upf): 2021/6/2 20:24
        """
        self.mediator.send(message, self)

    def notify(self, message):
        """
        @func name:
        @desc:
        @author: SAM
        @createTime: 2021/6/2 20:25
        @updateTime(upf): 2021/6/2 20:25
        """
        print('Colleague2 get a message: ', message)


class ConcreteMediator(Mediator):

    def send(self, message, col):
        """
        @func name:
        @desc:
        @author: SAM
        @createTime: 2021/6/2 20:25
        @updateTime(upf): 2021/6/2 20:25
        """
        if col == self.col1:
            self.col2.notify(message)
        else:
            self.col1.notify(message)


if __name__ == '__main__':
    m = ConcreteMediator()
    col1 = Colleague1(m)
    col2 = Colleague1(m)
    m.col1 = col1
    m.col2 = col2
    col1.send('How are you?')
    col2.send('Fine.')
