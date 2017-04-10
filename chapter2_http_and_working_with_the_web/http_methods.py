#!/usr/bin/env python

"""
Chapter2: HTTP methods
Page 160

----------------------

So far, we've been using requests for asking servers to send web resources to us,
but HTTP provides more actions that we can perform.
The GET in our request lines is an HTTP method, and there are several methods,
such as HEAD, POST, OPTION, PUT, DELETE, TRACE, CONNECT, and PATCH.

The HEAD method is the same as the GET method.
The only difference is that the server will never include a body in the response,
even if there is a valid resource at the requested URL.
The HEAD method is used for checking if a resource exists or if it has changed.
Note that some servers don't implement this method, but when they do,
it can prove to be a huge bandwidth saver.

"""

from urllib.request import Request, urlopen
from urllib.parse import urlencode


# HEAD method
# use alternative http methods with urllib by supplying the methond name to a request object
req = Request('http://www.basenet.com', method='HEAD')
response = urlopen(req)
print("[*] {}".format(response.status))
print("[*] {}".format(response.read()))


# POST method
data_dict = {'P': 'Python'}
# posting html form data requires formatting like querystrings in urls.
# this means urlencoding must be used
data = urlencode(data_dict).encode('utf-8')
# contruct the request. adding our data as data keyword agrument will tell
# urllib that we went it to be the body of the request
# this will make the request use the POST method, rather than the GET method
req = Request('http://search.debian.org/cgi-bin/omega', data=data)
# add Content-Type header
req.add_header('Content-Type', 'application/x-www-form-urlencode; charset=UTF-8')
# submit the request
response = urlopen(req)
print("[*] {}".format(response.read()))
