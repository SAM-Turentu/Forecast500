# -*- coding: utf-8 -*-
# Author: SAM
# Email: SAM-Turentu@outlook.com
# Name: Forecast500
# Filename: SourceDataService
# CreateTime: 2021/4/29 21:19
# Summary: ''
import json

from backend.utils.Result import ReturnJson
from dao.SoruceDataDAO import SourceDataDAO
from service.BaseService import BaseService


class SourceDataService(BaseService):

    def __init__(self):
        """
        @func name:
        @desc:
        @author: SAM
        @createTime: 2021/4/29 21:20
        @updateTime(upf): 2021/4/29 21:20
        """
        self.sourceDataDAO = SourceDataDAO.getInstance()

    async def insert_source_data_service(self, data):
        """
        @func name:
        @desc:
        @author: SAM
        @createTime: 2021/4/29 21:21
        @updateTime(upf): 2021/4/29 21:21
        """
        await self.sourceDataDAO.insert_data(data)
        return ReturnJson.success()

    async def withdraw_data_from_txt(self, data):
        """
        @func name:
        @desc:
        @author: SAM
        @createTime: 2021/5/6 20:58
        @updateTime(upf): 2021/5/6 20:58
        """
        _insert = {
            'term': data[0],
            'ball': list(data[1:]),
            'red_ball': list(data[1:-1]),
            'red_1': data[1],
            'red_2': data[2],
            'red_3': data[3],
            'red_4': data[4],
            'red_5': data[5],
            'red_6': data[6],
            'blue': data[7],
        }
        _ret = await self.sourceDataDAO.insert_data(_insert)
        return ReturnJson.success(data=data)

    # region Award Function
    async def insert_first_award(self, data):
        """
        @func name:
        @desc: 6 + 1 全中   --> 浮动
        @author: SAM
        @createTime: 2021/5/6 22:35
        @updateTime(upf): 2021/5/6 22:35
        """
        _insert = {

        }
        _ret = await self.sourceDataDAO.insert_data(_insert)

    async def insert_second_award(self, data):
        """
        @func name:
        @desc: 6 + 0   --> 浮动
        @author: SAM
        @createTime: 2021/5/6 22:35
        @updateTime(upf): 2021/5/6 22:35
        """
        _insert = {

        }
        _ret = await self.sourceDataDAO.insert_data(_insert)

    async def insert_third_award(self, data):
        """
        @func name:
        @desc: 5 + 1   --> 3000元
        @author: SAM
        @createTime: 2021/5/6 22:35
        @updateTime(upf): 2021/5/6 22:35
        """
        _insert = {

        }
        _ret = await self.sourceDataDAO.insert_data(_insert)

    async def insert_four_award(self, data):
        """
        @func name:
        @desc: 5 + 0 / 4 + 1   --> 200元
        @author: SAM
        @createTime: 2021/5/6 22:35
        @updateTime(upf): 2021/5/6 22:35
        """
        _insert = {

        }
        _ret = await self.sourceDataDAO.insert_data(_insert)

    async def insert_five_award(self, data):
        """
        @func name:
        @desc: 4 + 0 / 3 + 1   --> 10元
        @author: SAM
        @createTime: 2021/5/6 22:35
        @updateTime(upf): 2021/5/6 22:35
        """
        _insert = {

        }
        _ret = await self.sourceDataDAO.insert_data(_insert)

    async def insert_data_six_award(self, data):
        """
        @func name: 六等奖插入mongodb
        @desc: 2 + 1 / 1 + 1 / 0 + 1   必有一个blue   --> 5元
        @author: SAM
        @createTime: 2021/5/6 22:35
        @updateTime(upf): 2021/5/6 22:35
        """
        _insert = {

        }
        _ret = await self.sourceDataDAO.insert_data(_insert)

    # endregion

    async def find_all_data(self):
        """
        @func name: 查询集合所有数据
        @desc:
        @author: SAM
        @createTime: 2021/5/7 19:15
        @updateTime(upf): 2021/5/7 19:15
        """
        all_data = await self.sourceDataDAO.query_all_data()
        # item = await all_data.to_list(length=5000)
        _ret = []
        red_dict = {}
        blue_dict = {}
        for item in await all_data.to_list(length=5000):
            item.pop('_id')
            red_ball_list = item.get('red_ball')
            for i in red_ball_list:
                red_dict.setdefault(i, 0)
                red_dict[i] += 1

            blue_ball = item.get('blue')
            blue_dict.setdefault(blue_ball, 0)
            blue_dict[blue_ball] += 1

            _ret.append(item)

        red_length = sum(red_dict.values())
        blue_length = sum(blue_dict.values())
        red_dict = dict(sorted(red_dict.items()))
        blue_dict = dict(sorted(blue_dict.items()))
        print(red_dict)
        print(red_length)
        print(blue_dict)
        print(blue_length)
        # return ReturnJson.success(data=json.dumps(_ret))
        return ReturnJson.success(data=json.dumps(red_dict))



