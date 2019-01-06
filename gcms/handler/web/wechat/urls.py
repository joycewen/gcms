# coding: utf-8

from .views import WechatCallback

wechat_urls = [
    (r'/oauth/wechat_callback', WechatCallback),
]
