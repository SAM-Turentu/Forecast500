# -*- coding: utf-8 -*-
# Author: SAM
# Email: SAM-Turentu@outlook.com
# Name: Forecast500
# Filename: LoginForm
# CreateTime: 2021/7/13 15:36
# Summary: ''
from forms.BaseForm import *
from forms.MainForm import MainForm


class LoginForm(MainForm):

    def __init__(self):
        """
        @Author: SAM
        @CreateTime: 2021/7/13 15:36
        @UpdateTime(upf): 2021/7/13 15:36
        @Desc: ''
        """
        self.userPhone = String('手机号', validators=[DataRequired('手机号必填'), Length(11, 11, '手机号长度为11位')])
        self.userPassword = String('密码', validators=[DataRequired('密码必填'), Length(6, 16, '密码长度为6-16位')])
        # self.SMSCode = String('验证码', validators=[DataRequired('验证码必填'), Length(6, 6, '验证码长度为6位')])
        self.SMSCode = String('验证码')
