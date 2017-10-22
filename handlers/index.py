#!/usr/bin/env python
# encoding=utf8
import json
from tornado.web import RequestHandler


class IndexHandler(RequestHandler):
    def get(self, *args, **kwargs):
        result = {'hello': 'world'}
        return self.write(json.dumps(result))
