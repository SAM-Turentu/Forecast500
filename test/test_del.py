# -*- coding: utf-8 -*-
# Author: SAM
# Email: SAM-Turentu@outlook.com
# Name: Forecast500
# Filename: test_del
# CreateTime: 2022/5/12 17:11
# Summary: ''


import getpass


class WordApp(object):
    # def __new__(cls, *args, **kwargs):
    #     if cls.__instance is None:
    #         cls.__instance = super().__new__(cls)
    #     return cls.__instance
    _instance = None
    _flag = None

    @classmethod
    def getInstance(cls, visible=False, display_alerts=False):
        if cls._instance is None:
            cls._instance = cls(visible, display_alerts)
        return cls._instance

    def __init__(self, visible=False, display_alerts=False):
        # if not self.__flag:
        if not self._flag:
            try:
                self.app = 123
            except AttributeError:
                username = getpass.getuser()
                f_loc = r'C:\Users\{username}\AppData\Local\Temp\gen_py'.format(username=username)
                self.app = f_loc
                self.app.Visible = visible
                self.app.DisplayAlerts = display_alerts
            self._flag = True

    def __del__(self):
        try:
            print('failure')
        except Exception as e:
            print(e)


class Word(object):

    def __init__(self, docx_path=None, repair=True):
        self.docx_path = docx_path
        self.word_app = WordApp.getInstance()
        self.app = self.word_app.app
        if docx_path:
            self.document = self.app
        else:
            self.document = self.app

    def __del__(self):
        try:
            print('self.document: ', self.docx_path)
            del self.word_app
        except Exception as e:
            print('__del__', e)

    def __str__(self):
        return str(self.docx_path)


def main():
    word1 = Word('path1', repair=False)
    del word1
    word2 = Word('path2', repair=False)
    del word2
    print(123123)


if __name__ == '__main__':
    main()
