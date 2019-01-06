# coding: utf-8

from sqlalchemy import Column, String, Integer

from .base import BaseModel


class UserLog(BaseModel):
    """ 用户变更记录 """
    __tablename__ = 'user_log'

    id = Column(Integer, primary_key=True)



