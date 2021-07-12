# -*- coding: utf-8 -*-
# Author: SAM
# Email: SAM-Turentu@outlook.com
# Name: Forecast500
# Filename: test
# CreateTime: 2021/6/18 9:58
# Summary: ''



import datetime

import jwt


# def create_token(self, **kwargs):
def create_token():
    """
    @Author: SAM
    @CreateTime: 2021/6/25 15:29
    @UpdateTime(upf): 2021/6/25 15:29
    @Desc: ''
    """
    token_endpoint = 'http://192.168.1.141:8001'
    payload = {
        'id': None,
        'exp': datetime.datetime.utcnow() + datetime.timedelta(days=7),
        'iat': datetime.datetime.utcnow(),
        'iss': 'SAM',
        'data': {

        },
    }
    secret = 'secret_jwt'  # CONF.settings.secret_jwt
    # token = jwt.encode(payload=payload, key=secret, algorithm='HS256', headers=None, json_encoder=None)
    auth_token = jwt.encode(payload=payload, key=secret, algorithm='HS256')
    print(auth_token)
    return auth_token


# class Token:

if __name__ == '__main__':
    create_token()
