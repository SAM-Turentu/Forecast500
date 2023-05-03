# -*- coding: utf-8 -*-
# Author: SAM
# Email: SAM-Turentu@outlook.com
# Name: Forecast500
# Filename: test_pandas
# CreateTime: 2021/8/19 13:04
# Summary: ''


import time

import pandas as pd


def main():
    """
    @Author: SAM
    @CreateTime: 2021/8/19 13:05
    @UpdateTime(upf): 2021/8/19 13:05
    @Desc: ''
    """
    data = pd.read_csv('C:\\Users\\SAM-t\\Desktop\\new_data.csv', encoding='GB2312', dtype=str)
    # data = pd.read_csv('C:\\Users\\SAM-t\\Desktop\\nba.csv')
    # data = pd.read_csv('C:\\Users\\SAM-t\\Desktop\\nba.csv', encoding='utf-8')
    print(data.to_string())
    print(111)


if __name__ == '__main__':
    main()
