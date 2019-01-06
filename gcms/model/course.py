# coding: utf-8

from sqlalchemy import Column, Integer, String, BOOLEAN, TIMESTAMP, Text, text, DateTime

from .base import BaseModel


class Course(BaseModel):
    """ 课程 """
    __tablename__ = "course"

    id = Column(Integer, primary_key=True)
    name = Column(String(64), nullable=False)
    brand_id = Column(Integer, nullable=False, doc='品牌id')
    course_type = Column(Integer, nullable=False)
    duration = Column(Integer, doc='时长')
    max_member = Column(Integer, doc='最多上课人数')
    min_member = Column(Integer, doc='最少上课人数')
    desc = Column(String(128), doc='描述')
    cover_image = Column(String(128))
    media = Column(Text)
    creator = Column(Integer, doc='创建人')
    create_time = Column(DateTime)
    update_time = Column(DateTime)


class Schedule(BaseModel):
    """ 课表 """
    __tablename__ = 'schedule'

    id = Column(Integer, primary_key=True)
    course_id = Column(Integer, nullable=False, doc='课程id')
    teacher_id = Column(Integer, nullable=False, doc='教师id')  # 会不会有联合授课,一节课多个老师
    place_id = Column(Integer, nullable=False, doc='场馆id')
    classroom_id = Column(Integer, nullable=False, doc='教室id')
    max_member = Column(Integer, doc='最多上课人数')
    min_member = Column(Integer, doc='最少上课人数')
    start_time = Column(DateTime, nullable=False)
    end_time = Column(DateTime, nullable=False)
    order_time = Column(DateTime, doc='开放预约时间')
    payment_id = Column(Integer, doc='支付方式')


class ActivityRecord(BaseModel):
    """ 上课记录 """
    __tablename__ = 'activity_record'

    id = Column(Integer, primary_key=True)
    schedule_id = Column(Integer, nullable=False, doc='课id')
    card_id = Column(Integer, nullable=False, doc='卡id')
