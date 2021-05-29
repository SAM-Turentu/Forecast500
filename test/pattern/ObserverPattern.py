# -*- coding: utf-8 -*-
# Author: SAM
# Email: SAM-Turentu@outlook.com
# Name: Forecast500
# Filename: ObserverPattern
# CreateTime: 2021/5/26 17:08
# Summary: ''


"""
ObserverPattern
观察者模式
    特点：定义了一种一对多的关系，让多个观察对象同时监听一个主题对象，当主题对象状态发生变化时会通知所有观察者
"""


class Observer:

    def __init__(self, strname, strsub):
        """
        @author: SAM
        @CreateTime: 2021/5/26 17:20
        @UpdateTime(upf): 2021/5/26 17:20
        @desc: ''
        """
        self.name = strname
        self.sub = strsub

    def update(self):
        """
        @author: SAM
        @CreateTime: 2021/5/26 17:21
        @UpdateTime(upf): 2021/5/26 17:21
        @desc: ''
        """
        ...


class StockObserver(Observer):

    def update(self):
        """
        @author: SAM
        @CreateTime: 2021/5/26 17:21
        @UpdateTime(upf): 2021/5/26 17:21
        @desc: ''
        """
        print(f'{self.name}: {self.sub.action}, stop watching Stock and go on work!')


class NBAObserver(Observer):

    def update(self):
        """
        @author: SAM
        @CreateTime: 2021/5/26 17:22
        @UpdateTime(upf): 2021/5/26 17:22
        @desc: ''
        """
        print(f'{self.name}: {self.sub.action}, stop watching NBA and go on work!')


class SecretaryBase:

    def __init__(self):
        """
        @author: SAM
        @CreateTime: 2021/5/26 17:23
        @UpdateTime(upf): 2021/5/26 17:23
        @desc: ''
        """
        self.observers = []

    def attach(self, new_observer):
        """
        @author: SAM
        @CreateTime: 2021/5/26 17:24
        @UpdateTime(upf): 2021/5/26 17:24
        @desc: ''
        """

    def notify(self):
        """
        @author: SAM
        @CreateTime: 2021/5/26 17:24
        @UpdateTime(upf): 2021/5/26 17:24
        @desc: ''
        """


class Secretary(SecretaryBase):

    def attach(self, new_observer):
        """
        @author: SAM
        @CreateTime: 2021/5/26 17:25
        @UpdateTime(upf): 2021/5/26 17:25
        @desc: ''
        """
        self.observers.append(new_observer)

    def notify(self):
        """
        @author: SAM
        @CreateTime: 2021/5/26 17:25
        @UpdateTime(upf): 2021/5/26 17:25
        @desc: ''
        """
        for p in self.observers:
            p.update()


if __name__ == '__main__':
    p = Secretary()
    s1 = StockObserver('xh', p)
    s2 = NBAObserver('wyt', p)
    p.attach(s1)
    p.attach(s2)
    p.action = 'WARNING:BOSS'
    p.notify()
