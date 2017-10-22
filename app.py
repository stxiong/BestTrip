#!/usr/bin/env python
# encoding=utf8
import json
import tornado
import os
import tornado.httpserver
import tornado.ioloop
import tornado.web
from handlers.index import IndexHandler 

url_patterns = [
    (r'/', IndexHandler),
]

class App(tornado.web.Application):
    def __init__(self):
        app = tornado.web.Application.__init__(self, url_patterns)

if __name__ == '__main__':
    app = App()
    http_server = tornado.httpserver.HTTPServer(app)
    http_server.listen(8888)
    io_loop = tornado.ioloop.IOLoop.instance()
    io_loop.start()
