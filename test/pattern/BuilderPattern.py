# -*- coding: utf-8 -*-
# Author: SAM
# Email: SAM-Turentu@outlook.com
# Name: Forecast500
# Filename: BuilderPattern
# CreateTime: 2021/5/26 14:42
# Summary: '建造者模式'


"""
BuilderPattern
建造者模式
    特点：讲一个复杂对象的构建与它的表示分离，使得同样的构建过程可以创建不同的表示
"""


class Person:

    def CreateHead(self):
        """
        @author: SAM
        @CreateTime: 2021/5/26 14:44
        @UpdateTime(upf): 2021/5/26 14:44
        @desc: ''
        """
        ...

    def CreateHand(self):
        """
        @author: SAM
        @CreateTime: 2021/5/26 16:46
        @UpdateTime(upf): 2021/5/26 16:46
        @desc: ''
        """
        ...

    def CreateBody(self):
        """
        @author: SAM
        @CreateTime: 2021/5/26 16:46
        @UpdateTime(upf): 2021/5/26 16:46
        @desc: ''
        """
        ...

    def CreateFoot(self):
        """
        @author: SAM
        @CreateTime: 2021/5/26 16:46
        @UpdateTime(upf): 2021/5/26 16:46
        @desc: ''
        """
        ...


class ThinPerson(Person):

    def CreateHead(self):
        """
        @author: SAM
        @CreateTime: 2021/5/26 16:47
        @UpdateTime(upf): 2021/5/26 16:47
        @desc: ''
        """
        print('thin head')

    def CreateHand(self):
        """
        @author: SAM
        @CreateTime: 2021/5/26 16:47
        @UpdateTime(upf): 2021/5/26 16:47
        @desc: ''
        """
        print('thin hand')

    def CreateBody(self):
        """
        @author: SAM
        @CreateTime: 2021/5/26 16:48
        @UpdateTime(upf): 2021/5/26 16:48
        @desc: ''
        """
        print('thin body')

    def CreateFoot(self):
        """
        @author: SAM
        @CreateTime: 2021/5/26 16:48
        @UpdateTime(upf): 2021/5/26 16:48
        @desc: ''
        """
        print('thin foot')


class ThickPerson(Person):

    def CreateHead(self):
        """
        @author: SAM
        @CreateTime: 2021/5/26 16:47
        @UpdateTime(upf): 2021/5/26 16:47
        @desc: ''
        """
        print('thick head')

    def CreateHand(self):
        """
        @author: SAM
        @CreateTime: 2021/5/26 16:47
        @UpdateTime(upf): 2021/5/26 16:47
        @desc: ''
        """
        print('thick hand')

    def CreateBody(self):
        """
        @author: SAM
        @CreateTime: 2021/5/26 16:48
        @UpdateTime(upf): 2021/5/26 16:48
        @desc: ''
        """
        print('thick body')

    def CreateFoot(self):
        """
        @author: SAM
        @CreateTime: 2021/5/26 16:48
        @UpdateTime(upf): 2021/5/26 16:48
        @desc: ''
        """
        print('thick foot')


class Director:

    def __init__(self, temp: Person):
        """
        @author: SAM
        @CreateTime: 2021/5/26 16:49
        @UpdateTime(upf): 2021/5/26 16:49
        @desc: ''
        """
        self.p = temp

    def Create(self):
        """
        @author: SAM
        @CreateTime: 2021/5/26 16:49
        @UpdateTime(upf): 2021/5/26 16:49
        @desc: ''
        """
        self.p.CreateHead()
        self.p.CreateHand()
        self.p.CreateBody()
        self.p.CreateFoot()


if __name__ == '__main__':
    p = ThickPerson()
    d = Director(p)
    d.Create()
