#!/usr/bin/env python

from urllib.request import urlopen, Request
from urllib.parse import urlencode

data_dict = {'q': 'dagje'}
data = urlencode(data_dict).encode('utf-8')

req = Request('http://www.ns.nl', data=data)
req.add_header('Content-Type', 'application/x-www-form-urlencode; charset=UTF-8')

response = urlopen(req)

with open('downloads/post_method.html', 'w') as f:
    line = response.readline().decode()
    while line:
        f.write(line)
        line = response.readline().decode()
