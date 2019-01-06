# coding: utf-8

from sqlalchemy import Column, Integer, String

from .base import BaseModel


class Brand(BaseModel):
    """ 品牌 """
    __tablename__ = 'brand'

    id = Column(Integer, primary_key=True)
    name = Column(String(64), nullable=False)
    logo = Column(String(128))
