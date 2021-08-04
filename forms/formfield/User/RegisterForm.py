# -*- coding: utf-8 -*-
# Author: SAM
# Email: SAM-Turentu@outlook.com
# Name: Forecast500
# Filename: RegisterForm
# CreateTime: 2021/6/23 11:06
# Summary: ''


from forms.BaseForm import *
from forms.MainForm import MainForm


class RegisterForm(MainForm):

    def __init__(self):
        """
        @Author: SAM
        @CreateTime: 2021/6/23 11:07
        @UpdateTime(upf): 2021/6/23 11:07
        @Desc: ''
        """
        self.userPhone = String('手机号', validators=[DataRequired('手机号必填'), Length(11, 11, '手机号长度为11位')])
        self.userPassword = String('密码', validators=[DataRequired('密码必填'), Length(6, 16, '密码长度为6-16位')])
        self.userName = String('用户名', validators=[DataRequired('姓名必填'), Length(2, 10, '用户名长度为2-10位')])
        self.userBirthday = DateTime(label='用户生日', message='', validators=[])
        self.userEmail = String('用户邮箱')
        self.userSex = String('用户性别')
        # self.userLoginTime = String('用户登录时间')
        # self.userDelete = String('用户删除')
        # self.userStatus = String('用户状态')
        # self.userDisable = String('用户禁用')
        self.userVIP = String('用户VIP')
        self.userSource = String('用户来源')
