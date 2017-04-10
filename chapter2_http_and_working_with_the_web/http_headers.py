#!/usr/bin/env python

"""
Chapter 2: HTTP headers
Page 117
"""

from urllib.request import urlopen

response = urlopen('http://www.google.com')

print(response.getheaders())
