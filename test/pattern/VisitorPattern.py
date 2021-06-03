# -*- coding: utf-8 -*-
# Author: SAM
# Email: SAM-Turentu@outlook.com
# Name: Forecast500
# Filename: VisitorPattern
# CreateTime: 2021/6/3 10:17
# Summary: '访问者模式'


"""
VisitorPattern
访问者模式
    特点：表示一个作用于某对象结构中的各元素的操作。它使你可以在不改变各元素的类的前提下定义作用于这些元素的新操作
"""


class Person:

    def Accept(self, visitor):
        """
        @author: SAM
        @CreateTime: 2021/6/3 10:22
        @UpdateTime(upf): 2021/6/3 10:22
        @desc: ''
        """
        ...


class Man(Person):

    def Accept(self, visitor):
        """
        @author: SAM
        @CreateTime: 2021/6/3 10:22
        @UpdateTime(upf): 2021/6/3 10:22
        @desc: ''
        """
        visitor.GetManConclusion(self)


class Woman(Person):

    def Accept(self, visitor):
        """
        @author: SAM
        @CreateTime: 2021/6/3 10:23
        @UpdateTime(upf): 2021/6/3 10:23
        @desc: ''
        """
        visitor.GetWomanConclusion(self)


class Action:

    def GetManConclusion(self, concreteElementA):
        """
        @author: SAM
        @CreateTime: 2021/6/3 10:23
        @UpdateTime(upf): 2021/6/3 10:23
        @desc: ''
        """
        ...

    def GetWomanConclusion(self, concreteElementB):
        """
        @author: SAM
        @CreateTime: 2021/6/3 10:24
        @UpdateTime(upf): 2021/6/3 10:24
        @desc: ''
        """
        ...


class Success(Action):

    def GetManConclusion(self, concreteElementA):
        """
        @author: SAM
        @CreateTime: 2021/6/3 10:24
        @UpdateTime(upf): 2021/6/3 10:24
        @desc: ''
        """
        print('男人成功时，背后有一个伟大的女人')

    def GetWomanConclusion(self, concreteElementB):
        """
        @author: SAM
        @CreateTime: 2021/6/3 10:25
        @UpdateTime(upf): 2021/6/3 10:25
        @desc: ''
        """
        print('女人成功时，背后有一个不成功的男人')


class Failure(Action):

    def GetManConclusion(self, concreteElementA):
        """
        @author: SAM
        @CreateTime: 2021/6/3 10:25
        @UpdateTime(upf): 2021/6/3 10:25
        @desc: ''
        """
        print('男人失败时，闷头喝酒，谁也不用劝')

    def GetWomanConclusion(self, concreteElementB):
        """
        @author: SAM
        @CreateTime: 2021/6/3 10:26
        @UpdateTime(upf): 2021/6/3 10:26
        @desc: ''
        """
        print('女人失败时，眼泪泪汪汪，谁也劝不了')


class ObjectStructure:

    def __init__(self):
        """
        @author: SAM
        @CreateTime: 2021/6/3 10:27
        @UpdateTime(upf): 2021/6/3 10:27
        @desc: ''
        """
        self.plist = []

    def Add(self, p):
        """
        @author: SAM
        @CreateTime: 2021/6/3 10:27
        @UpdateTime(upf): 2021/6/3 10:27
        @desc: ''
        """
        self.plist = self.plist + [p]

    def Display(self, act):
        """
        @author: SAM
        @CreateTime: 2021/6/3 10:27
        @UpdateTime(upf): 2021/6/3 10:27
        @desc: ''
        """
        for p in self.plist:
            p.Accept(act)


if __name__ == '__main__':
    os = ObjectStructure()
    os.Add(Man())
    os.Add(Woman())
    sc = Success()
    os.Display(sc)
    fl = Failure()
    os.Display(fl)
