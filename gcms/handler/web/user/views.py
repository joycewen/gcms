# coding: utf-8

from gcms.model.user import User
from gcms.handler.base import APIBaseHandler


class User(APIBaseHandler):
    def get(self):
        pass

    def post(self):
        name = self.argument('name')
        phone = self.argument('phone')
        email = self.argument('email', default='', allow_null=True)
        open_id = ''
        nickname = ''
        user = User(name=name, phone=phone, email=email)
        self.model.add(user)
        return {
            'user_id': user.id
        }

    def put(self):
        pass

    def delete(self, *args, **kwargs):
        pass
