# coding: utf-8

from sqlalchemy import Column, Integer, String, BOOLEAN, TIMESTAMP, Text, text, Float

from .base import BaseModel


class Place(BaseModel):
    """ 场馆 """
    __tablename__ = 'place'

    id = Column(Integer, primary_key=True)
    name = Column(String(64), nullable=False, doc='场馆名称')
    brand_id = Column(Integer, nullable=False, doc='品牌id')
    address = Column(String(128))
    area = Column(Float, doc='面积')
    room_id = Column(Text, doc='教室id列表')


class Classroom(BaseModel):
    """ 教室 """
    __tablename__ = 'classroom'

    id = Column(Integer, primary_key=True)
    name = Column(String(64), nullable=False)
    capacity = Column(Integer, doc='可容纳最大人数')
    area = Column(Float(recision=2))
