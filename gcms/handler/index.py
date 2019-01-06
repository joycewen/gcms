# coding: utf-8

from .base import BaseHandler


class IndexHandler(BaseHandler):
    def get(self):
        self.write("Welcome to G-Steps Family!")
