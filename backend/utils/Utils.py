# -*- coding: utf-8 -*-
# Author: SAM
# Email: SAM-Turentu@outlook.com
# Name: Forecast500
# Filename: Utils
# CreateTime: 2021/5/17 20:03
# Summary: ''


import json
from datetime import datetime, date
from decimal import Decimal


class Utils(object):

    @staticmethod
    def JSONEncoder():
        """
        @func name:
        @desc: Json 序列化
        @author: SAM
        @createTime: 2021/5/17 20:04
        @updateTime(upf): 2021/5/17 20:04
        """

        class JSONEncoder(json.JSONEncoder):

            def default(self, obj):
                """
                @func name:
                @desc: Json 格式转换
                @author: SAM
                @createTime: 2021/5/17 20:08
                @updateTime(upf): 2021/5/17 20:08
                """
                if isinstance(obj, Decimal):
                    return float(obj)
                if isinstance(obj, datetime):
                    return str(obj)
                if isinstance(obj, date):
                    return str(obj)
                if isinstance(obj, set):
                    return str(obj, 'utf-8')
                if isinstance(obj, bytes):
                    return str(obj, 'utf-8')
                return json.JSONEncoder.default(self, obj)

        return JSONEncoder

    @staticmethod
    def GetCurrentDatetime():
        """
        @author: SAM
        @CreateTime: 2021/6/3 16:38
        @UpdateTime(upf): 2021/6/3 16:38
        @desc: '获取当前日期 - 时间'
        """
        return datetime.now()

    @staticmethod
    def FormTransferVO(success_dict: dict, vo):
        """
        @Author: SAM
        @CreateTime: 2021/6/23 13:42
        @UpdateTime(upf): 2021/6/23 13:42
        @Desc: 'form 转换为 vo'
        """
        for k, v in success_dict.items():
            vo.__setattr__(k, success_dict[k])
        return vo
