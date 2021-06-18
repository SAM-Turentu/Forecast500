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
    a = FieldName.__dict__
    b = {key: a[key] for key in a if '__' not in key}
    print(a)
    print(b)
