# -*- coding: utf-8 -*-
# Author: SAM
# Email: SAM-Turentu@outlook.com
# Name: Forecast500
# Filename: CombinationPattern
# CreateTime: 2021/5/29 19:07
# Summary: '组合模式'


"""
CombinationPattern
组合模式
   特点：将对象组合成树形结构，以表示“部分-整体”的层次关系，整体和单个组件使用方式具有一致性
"""


class Component:

    def __init__(self, strName):
        """
        @func name:
        @desc:
        @author: SAM
        @createTime: 2021/5/29 19:09
        @updateTime(upf): 2021/5/29 19:09
        """
        self.m_strName = strName

    def Add(self, com):
        """
        @func name:
        @desc:
        @author: SAM
        @createTime: 2021/5/29 19:10
        @updateTime(upf): 2021/5/29 19:10
        """
        ...

    def Display(self, nDepth):
        """
        @func name:
        @desc:
        @author: SAM
        @createTime: 2021/5/29 19:11
        @updateTime(upf): 2021/5/29 19:11
        """
        ...


class Leaf(Component):

    def Add(self, com):
        """
        @func name:
        @desc:
        @author: SAM
        @createTime: 2021/5/29 19:11
        @updateTime(upf): 2021/5/29 19:11
        """
        print('leaf can\'t add')

    def Display(self, nDepth):
        """
        @func name:
        @desc:
        @author: SAM
        @createTime: 2021/5/29 19:12
        @updateTime(upf): 2021/5/29 19:12
        """
        strtemp = ''
        for i in range(nDepth):
            strtemp = strtemp + '-'
        strtemp = strtemp + self.m_strName
        print(strtemp)


class Composite(Component):

    def __init__(self, strName):
        """
        @func name:
        @desc:
        @author: SAM
        @createTime: 2021/5/29 19:13
        @updateTime(upf): 2021/5/29 19:13
        """
        super().__init__(strName)
        self.m_strName = strName
        self.c = []

    def Add(self, com):
        """
        @func name:
        @desc:
        @author: SAM
        @createTime: 2021/5/29 19:13
        @updateTime(upf): 2021/5/29 19:13
        """
        self.c.append(com)

    def Display(self, nDepth):
        """
        @func name:
        @desc:
        @author: SAM
        @createTime: 2021/5/29 19:14
        @updateTime(upf): 2021/5/29 19:14
        """
        strtemp = ''
        for i in range(nDepth):
            strtemp = strtemp + '-'
        strtemp = strtemp + self.m_strName
        print(strtemp)
        for com in self.c:
            com.Display(nDepth + 2)


if __name__ == '__main__':
    p = Composite('Wong')
    p.Add(Leaf('Lee'))
    p.Add(Leaf('Zhao'))
    p1 = Composite('Wu')
    p1.Add(Leaf('San'))
    p.Add(p1)
    p.Display(1)
