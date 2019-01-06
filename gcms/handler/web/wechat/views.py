# coding: utf-8

import json
import requests

from tornado import httpclient, gen, web, auth

from gcms.utils import config

from gcms.handler.base import APIBaseHandler
from gcms.utils.cache import CacheManager

cache = CacheManager()


# 微信小程序
# CODE_API = 'https://open.weixin.qq.com/connect/qrconnect?' \
#        'appid=APPID&redirect_uri=REDIRECT_URI&response_type=code&scope=SCOPE&state=STATE#wechat_redirect'

# 微信公众号
CODE_API = 'https://open.weixin.qq.com/connect/oauth2/authorize?' \
           'appid=%s&redirect_uri=%s&response_type=code&scope=snsapi_userinfo&state=STATE#wechat_redirect'

ACCESS_TOKEN_API = 'https://api.weixin.qq.com/sns/oauth2/access_token?' \
            'appid=%s&secret=%s&code=%s&grant_type=authorization_code'

USER_INFO_API = 'https://api.weixin.qq.com/sns/userinfo?access_token=%s&openid=%s&lang=zh_CN'


class Wechat(object):
    def __init__(self):
        self.appid = config.get('wechat', 'appid')
        self.secret = config.get('wechat', 'secret')
        self.open_id = None
        self.access_token = None
        self.union_id = None
        self.user_info = None

    @staticmethod
    def url_get(url):
        res = requests.get(url)
        data = json.loads(res)
        return data

    def async_url_get(self, url):
        pass

    def get_code(self, redirect_uri):
        code_url = CODE_API % (self.appid, redirect_uri)

    def get_access_token(self, code):
        code_url = ACCESS_TOKEN_API % (self.appid, self.secret, code)

        res = Wechat.url_get(code_url)
        access_token = res['access_token']
        union_id = res['unionid']
        self.open_id = res['openid']
        self.access_token = access_token
        self.union_id = union_id
        return access_token

    def get_user_info(self):
        urls = USER_INFO_API % (
            self.access_token, self.open_id)
        res = Wechat.url_get(urls)
        user_info = {
            'open_id': res['openid'],
            'nickname': res['nickname'],
            'sex': res['sex'],
            'province': res['province'],
            'city': res['city'],
            'country': res['country'],
            'head_img_url': res['headimgurl'],
            'privilege': res['privilege'],
            'union_id': res['unionid']
        }
        self.user_info = user_info
        return user_info


class WechatCallback(APIBaseHandler):
    def get(self):
        pass


class WechatPay(APIBaseHandler):
    pass
