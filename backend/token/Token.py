# -*- coding: utf-8 -*-
# Author: SAM
# Email: SAM-Turentu@outlook.com
# Name: Forecast500
# Filename: token
# CreateTime: 2021/6/25 15:28
# Summary: ''


import time
import uuid
import jwt
from conf import CONF


class Token:

    def __init__(self):
        """
        @Author: SAM
        @CreateTime: 2021/6/29 14:49
        @UpdateTime(upf): 2021/6/29 14:49
        @Desc: ''
        """
        self.exp = CONF.token.token_exp  # 7天 = 3600 * 24 * 7 = 604800 s
        self.algorithm = CONF.token.token_algorithm  # HS256
        self.secret = CONF.token.token_secret
        self.issure = CONF.token.issure

    def create_token(self, **kwargs):
        """
        @Author: SAM
        @CreateTime: 2021/6/25 15:29
        @UpdateTime(upf): 2021/6/25 15:29
        @Desc: ''
        """
        current_time = time.time()
        payload = {
            'id': 'user.user_id',
            'exp': current_time + self.exp,
            'iat': current_time,
            'iss': self.issure,
            'data': {
                'user': kwargs.get('user'),
                'uuid': uuid.uuid4().__str__()
            },
        }
        auth_token = jwt.encode(payload, self.secret, self.algorithm)
        return auth_token

    def decode_token(self, token) -> dict:
        """
        @Author: SAM
        @CreateTime: 2021/6/28 16:03
        @UpdateTime(upf): 2021/6/28 16:03
        @Desc: ''
        """
        data = {}
        info = jwt.decode(token, self.secret, self.algorithm, issure=self.issure)
        if info:
            data = info['data']
        return data


TOKEN = Token()

# if __name__ == '__main__':
#     a = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpZCI6InVzZXIudXNlcl9pZCIsImV4cCI6MTYyNTYzOTgyNy40NjkzMzI1LCJpYXQiOjE2MjUwMzUwMjcuNDY5MzMyNSwiaXNzIjoiU0FNIiwiZGF0YSI6eyJ1c2VyIjoiU0FNIiwidXVpZCI6ImQ2NGRiOWUwLWI1YjItNDAzYy1iOWI1LWJkMDc5ZTRjZjlhZiJ9fQ.2-_4YtdCibh6ecCmUu4_LORdcNJiIYlGiGDE2WJ_jyA'
#     token = Token()
#     # token.create_token()
#     data = token.decode_token(a)
#     print(data)
