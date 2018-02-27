"""
All the spiders are used to validate ip resources.

Here are all the validator website
https://httpbin.org/ip
http://httpbin.org/ip
https://weibo.cn/

If you want to add your own validators,you must add all the queues
in config/settings.py and register tasks in config/rules.py,and add
the task key to HttpBinInitValidator's https_tasks or http_tasks
"""
from .httpbin import (
    HttpBinInitValidator, HttpValidator,
    HttpsValidator)

from .weibo import WeiBoValidator
