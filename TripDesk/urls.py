#!/usr/bin/env python
# encoding=utf8
from harbor import handlers

url_patterns = [
    (r'/', handlers.IndexHandler),
    (r'/index', handlers.IndexHandler),
    (r'/sku', handlers.SkuHandler),
    (r'/sku/purchase', handlers.SkuPurchaseHandler),
    (r'/goods', handlers.GoodsHandler),
    (r'/activity', handlers.ActivityHandler),
    (r'/activity/detail', handlers.ActivityDetailHandler),
    (r'/daily', handlers.DailyHandler),
]
