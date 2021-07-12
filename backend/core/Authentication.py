# -*- coding: utf-8 -*-
# Author: SAM
# Email: SAM-Turentu@outlook.com
# Name: Forecast500
# Filename: Authentication
# CreateTime: 2021/6/29 15:04
# Summary: ''


from backend.token.Token import TOKEN
from backend.utils.BaseReturn import ReturnJson


class BaseAuthentication:

    def authenticate(self, handler):
        """
        @Author: SAM
        @CreateTime: 2021/6/29 15:07
        @UpdateTime(upf): 2021/6/29 15:07
        @Desc: ''
        """


class Authentication(BaseAuthentication):

    def authenticate(self, handler):
        """
        @Author: SAM
        @CreateTime: 2021/6/29 15:09
        @UpdateTime(upf): 2021/6/29 15:09
        @Desc: ''
        """
        token = handler.request.headers.get('Authorization')
        if not token:
            raise ReturnJson.EXCEPTION(error_message='no token')
        info = TOKEN.decode_token(token)
        print(info)
