#!/usr/bin/env python

"""
Chapter 2: Handling problems
page 114
"""

import urllib.error
from urllib.request import urlopen

try:
    urlopen('http://www.ietf.org/rfc/rfc0.txt')
    # to create an example of an exception, use below line
    # urlopen('http://192.0.2.1/index.html')
except urllib.error.HTTPError as e:
    print('status', e.code)
    print('reason', e.reason)
    print('url', e.url)
