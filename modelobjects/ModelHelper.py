# -*- coding: utf-8 -*-
# Author: SAM
# Email: SAM-Turentu@outlook.com
# Name: Forecast500
# Filename: ModelHelper
# CreateTime: 2021/7/2 13:08
# Summary: ''


from modelobjects.do.userdo.RegisterDO import RegisterDO
from modelobjects.dto.userdto.RegisterDTO import RegisterDTO
from modelobjects.vo.uservo.RegisterVO import RegisterVO
from modelobjects.po.UserPO import UserPO


class ModelHelper:

    @classmethod
    def VOTransferDTO(cls, VO, DTO):
        """
        @Author: SAM
        @CreateTime: 2021/7/2 10:40
        @UpdateTime(upf): 2021/7/2 10:40
        @Desc: 'VO (View Object) 转为 DTO (Data Transfer Object)'
        """
        for key in DTO.__dict__.keys():
            DTO.__dict__[key] = VO.__getattribute__(key) if hasattr(VO, key) else None

    @classmethod
    def DTOTransferDO(cls, DTO: RegisterDTO, DO: RegisterDO):
        """
        @Author: SAM
        @CreateTime: 2021/7/2 13:12
        @UpdateTime(upf): 2021/7/2 13:12
        @Desc: 'DTO 转为 DO, DO 完成服务层的业务逻辑'
        """
        for k, v in DTO.__dict__.items():
            if k in DO.__dict__:
                DO.__dict__[k] = v

    @classmethod
    def DOTransferPO(cls, DO, PO):
        """
        @Author: SAM
        @CreateTime: 2021/7/2 13:12
        @UpdateTime(upf): 2021/7/2 13:12
        @Desc: ''
        """
        for k, v in DO.__dict__.items():
            if k in PO.__dict__:
                PO.__dict__[k] = v


def main():
    """
    @Author: SAM
    @CreateTime: 2021/7/2 13:24
    @UpdateTime(upf): 2021/7/2 13:24
    @Desc: ''
    """
    vo = RegisterVO()
    vo.userName = 'SAM'
    vo.userPhone = '18292007162'
    vo.userPassword = 'SAM-Password'

    dto = RegisterDTO()
    do = RegisterDO()
    po = UserPO()
    try:
        ModelHelper.VOTransferDTO(vo, dto)
        print(dto)
        ModelHelper.DTOTransferDO(dto, do)
        print(do)
        ModelHelper.DOTransferPO(do, po)
        print(po)
    except Exception as e:
        print('转换异常信息：', e)


if __name__ == '__main__':
    main()
