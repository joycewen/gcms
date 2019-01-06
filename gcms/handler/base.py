# coding: utf-8
import re
import json
from functools import wraps
from traceback import format_exc

import tornado.web

from gcms.utils.db import Configure
from gcms.utils.exception import BaseError, ServerError
from gcms.utils.logger import api_logger

logger = api_logger()


def handler(func):
    @wraps(func)
    def wrapper(self, *args, **kwargs):
        code, msg, res = 0, 'success', None
        try:
            res = func(self, *args, **kwargs)
        except BaseError, e:
            code, msg = e.split()
        except Exception, e:
            self.logger.error(format_exc())
            code, msg = 65535, 'UnHandler Error: {e}'.format(e=str(e))
        resp = {'code': code, 'msg': u'%s' % msg, 'res': res}
        resp = json.dumps(resp)
        api_logger().info(
            '%s: %s' % (self.__class__.__name__, re.sub(r'(\\n|\\|\s+)', '', resp)))
        self.write(resp)
    return wrapper


class BaseHandler(tornado.web.RequestHandler):
    def set_base_header(self):
        self.set_header('Cache-Control', 'private,no-cache,must-revalidate')

    def pre_render(self):
        self.set_base_header()

    def initialize(self):
        self.model = Configure()

    def on_finish(self):
        self.model.close()

    def argument(self, name, default=None, allow_null=False):
        r_body = self.request.body
        if not r_body:
            r_body = '{}'
        request_body = json.loads(r_body)
        if name not in request_body and not allow_null:
            raise ServerError(ServerError.ARGS_MISSING, args=name)
        return request_body.get(name, default)


class APIBaseHandler(BaseHandler):
    def set_api_header(self):
        self.set_header('Content-Type', 'application/json')
        self.set_header('Access-Control-Allow-Origin', '*')
        self.set_header('Access-Control-Allow-Methods', 'POST, GET, OPTIONS')
        self.set_header('Access-Control-Max-Age', 1000)
        self.set_header('Access-Control-Allow-Headers', '*')

    def pre_render(self):
        super(APIBaseHandler, self).pre_render()
        self.set_api_header()

    def render(self, data):
        self.pre_render()
        if isinstance(data, dict):
            data = json.dumps(data)
        self.write(data)
        if not self._finished:
            self.finish()


class PageBaseHandler(BaseHandler):
    def set_page_header(self):
        self.set_header('Content-Type', 'text/html;charset=utf-8')

    def pre_render(self):
        super(PageBaseHandler, self).pre_render()
        self.set_page_header()


def handler(fun):
    @wraps(fun)
    def wrapper(self, *args, **kwargs):
        code, msg, res = 0, 'success', None
        try:
            # if not self.session.get('open_id', ''):
            #     if self.__class__.__name__ != 'CheckloginHandler':
            #         raise ServerError(ServerError.USER_NO_LOGIN)
            res = fun(self, *args, **kwargs)
        except BaseError, e:
            code, msg = e.split()
        except Exception, e:
            self.logger.error(format_exc())
            code, msg = 65535, 'UnHandler Error: {e}'.format(e=str(e))
        resp = {'code': code, 'msg': u'%s' % msg, 'res': res}
        resp = json.dumps(resp)
        api_logger().info(
            '%s: %s' % (self.__class__.__name__, re.sub(r'(\\n|\\|\s+)', '', resp)))
        self.write(resp)

    return wrapper
