# coding: utf-8

import tornado.web
import tornado.ioloop

from gcms.urls import urls


def init_settings():
    pass


def start_application():
    app = tornado.web.Application(urls)
    app.listen(8080)
    tornado.ioloop.IOLoop.instance().start()


def run():
    init_settings()
    start_application()


if __name__ == '__main__':
    run()
