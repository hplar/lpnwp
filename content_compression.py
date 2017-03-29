#!/usr/bin/env python

"""
Chapter 2: Content compression
page 124 - 127
"""

from urllib.request import Request
from urllib.request import urlopen
import gzip


# define headers
headers = {
    'Accept-Encoding': 'gzip',
}

# create a request object and add headers
req = Request('http://www.debian.org', headers=headers)

# submit the request
response = urlopen(req)

# check if the server is using gzip compression
print("[*] {}".format(response.getheader('Content-Encoding')))

# show part of the compressed content
# print("[*] {}".format(response.read(128)))

# decompress the body data with the gzip module
content = gzip.decompress(response.read())

# view decompressed data
print("[*] {}".format(content.splitlines()[:5]))


# A REQUEST W/O COMPRESSION
headers = {
    'Accept-Encoding': 'identity',
}
req = Request('http://www.debian.org', headers=headers)
response = urlopen(req)
# Content-Encoding = None
print("[*] {}".format(response.getheader('Content-Encoding')))


# MULTIPLE VALUES (relative weightings can be applied)
encodings = 'gzip, deflate;q=0.8, identity;q=0.0'
req = Request('http://www.debian.org')
req.add_header('Accept-Encoding', encodings)
response = urlopen(req)
print("[*] {}".format(response.getheader('Content-Encoding')))

