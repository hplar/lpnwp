#!/usr/bin/env python

from urllib.request import Request, urlopen

headers = {
    'Accepted-Language': 'nl',
    'User-agent': 'bobbo',
}

req = Request('http://www.nu.nl', headers=headers)
response = urlopen(req)
response_headers = req.header_items()

for header in response_headers:
    print(header)
