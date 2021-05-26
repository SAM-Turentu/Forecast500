# -*- coding: utf-8 -*-
# Author: SAM
# Email: SAM-Turentu@outlook.com
# Name: Forecast500
# Filename: TemplateMethodPattern
# CreateTime: 2021/5/26 14:11
# Summary: '模板方法模式'


"""
TemplateMethodPattern
模板方法模式
    特点：定义一个操作中的算法骨架，将一些步骤延迟至子类中
"""


class TestPaper:

    def TestQuestion1(self):
        """
        @author: SAM
        @CreateTime: 2021/5/26 14:12
        @UpdateTime(upf): 2021/5/26 14:12
        @desc: ''
        """
        print('Test1: A. B. C. D.')
        print(f'({self.Answer1()})')

    def TestQuestion2(self):
        """
        @author: SAM
        @CreateTime: 2021/5/26 14:14
        @UpdateTime(upf): 2021/5/26 14:14
        @desc: ''
        """
        print('Test2: A. B. C. D.')
        print(f'({self.Answer2()})')

    def Answer1(self):
        """
        @author: SAM
        @CreateTime: 2021/5/26 14:13
        @UpdateTime(upf): 2021/5/26 14:13
        @desc: ''
        """
        return ''

    def Answer2(self):
        """
        @author: SAM
        @CreateTime: 2021/5/26 14:14
        @UpdateTime(upf): 2021/5/26 14:14
        @desc: ''
        """
        return ''


class TestPaperA(TestPaper):

    def Answer1(self):
        """
        @author: SAM
        @CreateTime: 2021/5/26 14:15
        @UpdateTime(upf): 2021/5/26 14:15
        @desc: ''
        """
        return 'B'

    def Answer2(self):
        """
        @author: SAM
        @CreateTime: 2021/5/26 14:15
        @UpdateTime(upf): 2021/5/26 14:15
        @desc: ''
        """
        return 'C'


class TestPaperB(TestPaper):

    def Answer1(self):
        """
        @author: SAM
        @CreateTime: 2021/5/26 14:16
        @UpdateTime(upf): 2021/5/26 14:16
        @desc: ''
        """
        return 'D'

    def Answer2(self):
        """
        @author: SAM
        @CreateTime: 2021/5/26 14:16
        @UpdateTime(upf): 2021/5/26 14:16
        @desc: ''
        """
        return 'D'


if __name__ == '__main__':
    s1 = TestPaperA()
    s2 = TestPaperB()
    print('student 1')
    s1.TestQuestion1()
    s1.TestQuestion2()
    print('student 2')
    s2.TestQuestion1()
    s2.TestQuestion2()
