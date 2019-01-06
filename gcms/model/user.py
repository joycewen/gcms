# coding: utf-8

""" 系统登录相关用户, 管理人员 """

from sqlalchemy import Column, Integer, String, BOOLEAN, text, DateTime

from .base import BaseModel


class User(BaseModel):
    """ 用户 """
    __tablename__ = "user"

    id = Column(Integer, primary_key=True)
    openid = Column(String(64), nullable=False, server_default=text("''"))
    name = Column(String(64), nullable=False, doc='姓名')
    phone = Column(String(16), nullable=False, doc='手机号')
    sex = Column(Integer, doc='性别')
    nickname = Column(String(64), server_default=text("''"), doc='昵称')

    email = Column(String(32))
    photo = Column(String(128), doc='头像')
    birthdate = Column(DateTime, doc='生日')
    address = Column(String(64))
    place_id = Column(Integer, doc='所属店')
    source_id = Column(Integer, doc='来源')
    referrer_id = Column(Integer, doc='推荐人')
    staff_id = Column(Integer, doc='销售')
    desc = Column(String(128))

    dance_type = Column(String(64), doc='舞种')

    login_time = Column(DateTime, doc='最近一次登录时间')
    login_ip = Column(String(64), doc='最近一次登录ip')
    is_del = Column(BOOLEAN, nullable=False, server_default=0, doc="逻辑删除, true(删除)|false(未删除)")
    create_time = Column(DateTime, nullable=False, doc='注册时间')
    update_time = Column(DateTime, nullable=False)
    brand_id = Column(Integer, nullable=False, doc='品牌')
    role_id = Column(Integer, nullable=False, doc='角色')


class Role(BaseModel):
    """ 角色 """
    __tablename__ = 'role'

    id = Column(Integer, primary_key=True)
    name = Column(String(32), nullable=False)
    icon = Column(String(128))
