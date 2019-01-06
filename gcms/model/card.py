# coding: utf-8

from sqlalchemy import Column, Integer, String, BOOLEAN, Text, Float, DateTime

from .base import BaseModel


class Price(BaseModel):
    """ 价格 """
    __tablename__ = "price"

    id = Column(Integer, primary_key=True)
    counts = Column(Integer, nullable=False, doc='充值次数')
    amount = Column(Integer, nullable=False, default=0, doc='金额额度')  # 预留字段
    paid = Column(Float(recision=2), nullable=False, doc='实收价格')
    expire = Column(Integer, nullable=False, doc='有效期')
    desc = Column(String(64), default='', doc='说明')
    support_type = Column(Text, doc='支持类型')
    card_category_id = Column(Integer, nullable=False, doc='会员卡种类')
    create_time = Column(DateTime)
    update_time = Column(DateTime)


class CardCategory(BaseModel):
    """ 会员卡种类 """

    __tablename__ = 'card_category'

    id = Column(Integer, primary_key=True)
    name = Column(String(32), nullable=False)
    card_type = Column(Integer, nullable=False, doc='卡类型')  # 次卡
    brand_id = Column(Integer, nullable=False, doc='品牌id')
    place_id = Column(Integer, nullable=False, doc='场馆id')
    priority = Column(Integer, nullable=True, default=0, doc='权重')
    desc = Column(String(64), nullable=True, default='', doc='简介')
    limit_order_count = Column(Integer, nullable=True, default=0, doc='限制可提前预约课程数')
    limit_card_count = Column(Integer, nullable=True, default=1, doc='限制可购买会员卡数')
    limit_course = Column(Text, doc='限制周期内约课')
    tos = Column(BOOLEAN, default=1, doc='服务条款')


class Card(BaseModel):
    """ 会员卡 """
    __tablename__ = "card"

    id = Column(Integer, primary_key=True)
    category_id = Column(Integer, nullable=False, doc='会员卡种类id')
    user_id = Column(Integer, nullable=False, doc='绑定会员')
    price_id = Column(Integer, nullable=False, doc='价格id')
    card_id = Column(String(64), doc='实体卡号')
    remain_count = Column(Integer, nullable=False, default=0)
    create_time = Column(DateTime, nullable=False, doc='开卡时间')
    expire_time = Column(DateTime, nullable=False, doc='过期时间')
    payment_id = Column(Integer, nullable=False, doc='支付方式')
    staff_id = Column(Integer, nullable=False, doc='工作人员')
    desc = Column(String(64), doc='备注信息')
