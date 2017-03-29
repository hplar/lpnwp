#!/usr/bin/env python

"""
Chapter 2: Customizing requests
Page: 121
"""

from urllib.request import Request
from urllib.request import urlopen

# create request object
req = Request('http://www.debian.org')

# add language header
req.add_header('Accept-Language', 'sv')

# submit the customized request
response = urlopen(req)

# check whether it's really in Swedish
print("[*] {}".format(response.readlines()[:5]))

# view request headers (urlopen adds some headers on its own)
print("[*] {}".format(req.header_items()))

# shortcut for adding headers: add them when we create the request object
headers = {'Accept-Language': 'sv'}
req = Request('http://www.debian.org', headers=headers)
print("[*] {}".format(req.header_items()))
