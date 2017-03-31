#!/usr/bin/env python

"""
Chapter 2: URLs
Page 146
"""

from urllib.parse import urlparse

result = urlparse('http://www.python.org/dev/peps')
print("[*] {}".format(result))

# print only the network location
print("[*] {}".format(result.netloc))

# print only the path at the network location
print("[*] {}".format(result.path))

# manually add a port number (default http: 80, default https: 443)
result = urlparse('http://www.python.nl:8080/')
print("[*] {}".format(result))


