# -*- coding: utf-8 -*-
# Author: SAM
# Email: SAM-Turentu@outlook.com
# Name: Forecast500
# Filename: test
# CreateTime: 2021/6/18 9:58
# Summary: ''


class FieldName:
    label = 'asdf'
    en_name = None


if __name__ == '__main__':
    a = FieldName()
    b = FieldName()
    print(hasattr(a, 'en_name'))
    print(hasattr(b, 'label'))
    # if 'asdf' in a.label:
    #     print(111)
    # else:
    #     print(222)
