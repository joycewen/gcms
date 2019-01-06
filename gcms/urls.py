# coding: utf-8

from .handler.index import IndexHandler
from .handler.web.wechat.urls import wechat_urls
from .handler.web.card.urls import card_urls
from .handler.web.course.urls import course_urls
from .handler.web.user.urls import user_urls

urls = [
    (r'/', IndexHandler),
]

urls += wechat_urls
urls += card_urls
urls += course_urls
urls += user_urls
