# -*- coding: utf-8 -*-
# Author: SAM
# Email: SAM-Turentu@outlook.com
# Name: Forecast500
# Filename: InterpreterPattern
# CreateTime: 2021/6/3 10:01
# Summary: '解释器模式'


"""
InterpreterPattern
解释器模式
    特点：给定一个语言，定义它的文法的一种表示，并定义一个解释器，这个解释器使用该表示来解释语言中的句子
"""


class Context:

    def __init__(self):
        """
        @author: SAM
        @CreateTime: 2021/6/3 10:03
        @UpdateTime(upf): 2021/6/3 10:03
        @desc: ''
        """
        self.input = ''
        self.output = ''


class AbstractExpression:

    def Interpret(self, context):
        """
        @author: SAM
        @CreateTime: 2021/6/3 10:03
        @UpdateTime(upf): 2021/6/3 10:03
        @desc: ''
        """
        ...


class Expression(AbstractExpression):

    def Interpret(self, context):
        """
        @author: SAM
        @CreateTime: 2021/6/3 10:04
        @UpdateTime(upf): 2021/6/3 10:04
        @desc: ''
        """
        print('terminal interpret')


class NonterminalExpression(AbstractExpression):

    def Interpret(self, context):
        """
        @author: SAM
        @CreateTime: 2021/6/3 10:04
        @UpdateTime(upf): 2021/6/3 10:04
        @desc: ''
        """
        print('Nonterminal interpret')


if __name__ == '__main__':
    context = ''
    c = []
    c = c + [Expression()]
    c = c + [NonterminalExpression()]
    c = c + [Expression()]
    c = c + [Expression()]
    for a in c:
        a.Interpret(context)
