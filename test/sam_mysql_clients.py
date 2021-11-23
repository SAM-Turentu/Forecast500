# -*- coding: utf-8 -*-
# Author: SAM
# Email: SAM-Turentu@outlook.com
# Name: Forecast500
# Filename: sam_mysql_clients
# CreateTime: 2021/10/27 18:51
# Summary: ''


from sqlalchemy import *
from sqlalchemy.orm import declarative_base, scoped_session, sessionmaker

engine = create_engine('mysql+pymysql://root:123456@localhost:3306/test_db?charset=utf8')
session = scoped_session(sessionmaker(autocommit=False, autoflush=False, bind=engine))

Base = declarative_base()


class User2(Base):
    __tablename__ = 'user'
    __table_args__ = {'schema': 'test_db2'}

    id = Column(Integer, primary_key=True)
    user = Column(String(20))


class User(Base):
    __tablename__ = 'user'
    __table_args__ = {'schema': 'test_db'}

    id = Column(Integer, primary_key=True)
    name = Column(String(20))


class TestUser(User):
    __table_args__ = {'schema': 'test_db2'}


def create_user():
    """
    @func name:
    @desc:
    @author: SAM
    @createTime: 2021/10/27 19:04
    @updateTime(upf): 2021/10/27 19:04
    """
    try:
        host = 'localhost'
        port = '3306'
        user = 'root'
        password = '123456'
        db = 'test_db'

        engine_str = f'mysql+pymysql://{user}:{password}@{host}:{port}/{db}?charset=utf8'

        name = 'SAM'
        model = User(id=1, name=name)
        session.add(model)
        model2 = User2(id=1, user=name)
        session.add(model2)
        session.commit()
    except Exception as e:
        session.rollback()
        print(e)


if __name__ == '__main__':
    create_user()
