# -*- coding: utf-8 -*-
# Author: SAM
# Email: SAM-Turentu@outlook.com
# Name: Forecast500
# Filename: RegisterVO
# CreateTime: 2021/6/23 13:23
# Summary: ''


class RegisterVO(object):

    def __init__(self):
        self._userPhone = None
        self._userName = None
        self._password = None

    @property
    def userPhone(self):
        return self._userPhone

    @userPhone.setter
    def userPhone(self, value):
        self._userPhone = value

    @property
    def userName(self):
        return self._userName

    @userName.setter
    def userName(self, value):
        self._userName = value

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, value):
        self._password = value


class registerVO:
    userName: str = None
    userPhone: str = None
    password: str = None


# region Description
def FormTransferVO(success_dict: dict, vo):
    """
    @Author: SAM
    @CreateTime: 2021/6/23 13:42
    @UpdateTime(upf): 2021/6/23 13:42
    @Desc: ''
    """
    for k, v in success_dict.items():
        vo.__setattr__(k, success_dict[k])
    return vo


def main():
    """
    @Author: SAM
    @CreateTime: 2021/6/23 13:24
    @UpdateTime(upf): 2021/6/23 13:24
    @Desc: ''
    """
    success_dict = {
        'userName': 'SAM',
        'password': 'SAM-224534',
        'userPhone': '18292007162',
    }
    b = registerVO()
    FormTransferVO(success_dict, b)
    print(b.__dict__)
    print(b.userPhone)
    print(b.userName)
    print(b.password)


if __name__ == '__main__':
    main()
# endregion
