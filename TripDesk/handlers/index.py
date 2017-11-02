#!/usr/bin/env python
# encoding=utf8
import json
from tornado.web import RequestHandler
from tornado import template


class IndexHandler(RequestHandler):
    def get(self, *args, **kwargs):
        loader = template.Loader("templates")
        return self.write(loader.load("ticket_box.html").generate())
