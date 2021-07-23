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
import time
import pbkdf2
import hashlib
if __name__ == '__main__':
    # create_token()
    for _ in range(20):
        s = time.time()
        # a = pbkdf2.crypt('pwd', iterations=0x256)  # 耗时严重
        a = pbkdf2.crypt('1234567890', iterations=0x256)  # 耗时严重  pbkdf2:sha256
        # a = pbkdf2.crypt('pwd', iterations=0x2537)  # 耗时严重
        print(a)
        e = time.time()
        print('加密算法耗时：', e - s)  # 耗时0.4s

        # s = time.time()
        # a = hashlib.sha256('value'.encode())
        # hashlib.pbkdf2_hmac(hash_name='sha256', password='value'.encode(), salt=b'123', iterations=256)
        # encrypts = a.hexdigest()
        # e = time.time()
        # print(encrypts)
        # print(f'加密算法耗时：{e} - {s} = ', e - s)  # 耗时0.4s

