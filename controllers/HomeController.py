# -*- coding: utf-8 -*-
# Author: SAM
# Email: SAM-Turentu@outlook.com
# Name: Forecast500
# Filename: HomeController
# CreateTime: 2021/4/27 21:59
# Summary: ''


import ast
import json
from backend.core.Basehandler import BaseHandler
from backend.core.RouteHandler import Route
from backend.token.Token import TOKEN
from backend.utils.BaseReturn import ReturnJson
from backend.utils.Decorate import Return, Auth
from service.SourceDataService import SourceDataService


@Route(r'/')
class HomeHandler(BaseHandler):
    """
    @interface name:
    @desc:
    @author: SAM
    @createTime: 2021/4/27 22:01
    @updateTime(upf): 2021/4/27 22:01
    """

    @Return
    @Auth
    async def get(self):
        user = None
        json_dict = self.json_dict
        value = self.get_argument('value')
        print('value: ', value)
        # token = TOKEN.create_token(user='SAM')
        return ReturnJson.SUCCESS(data=value)

        # sourceDataService = SourceDataService()
        # result = await sourceDataService.insert_source_data_service(doc)
        # if result:
        #     ...
        # else:  # 插入失败
        #     ...
        # return self.write(json.dumps(doc))

        # return ReturnJson.SUCCESS(data=result)


@Route('/all')
class FindAllDataHandler(BaseHandler):
    """
    @interface name:
    @desc:
    @author: SAM
    @createTime: 2021/5/7 19:19
    @updateTime(upf): 2021/5/7 19:19
    """

    @Return
    async def get(self):
        sourceService = SourceDataService()
        # all_data = await sourceService.find_all_data()
        return await sourceService.find_all_data()


@Route(r'/zy')
class HomeHandler(BaseHandler):
    """
    @interface name:
    @desc:
    @author:
    @createTime: 2021/10/24 19:12
    @updateTime(upf): 2021/10/24 19:12
    """

    async def get(self):
        if not self.get_cookie('zy_user'):
            self.redirect('/login')
        self.render('index.html')


@Route(r'/login')
class LoginHandler(BaseHandler):
    """
    @interface name:
    @desc:
    @author:
    @createTime: 2021/10/24 19:12
    @updateTime(upf): 2021/10/24 19:12
    """

    async def get(self):
        self.render('login.html')

    async def post(self):
        phone = self.get_body_argument('phone')
        print(f'章燕的手机号：{phone}')
        if phone:
            self.set_cookie('zy_user', 'WelcomeLogin')
            self.redirect('/')
        else:
            self.redirect('/login')
