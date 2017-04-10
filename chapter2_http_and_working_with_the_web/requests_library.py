#!/usr/bin/env python

"""
Chapter 2: The Requests Library
Page: 169

-------------------------------

The third-party library Requests has been developed to improve upon the urllib standard library.
The Requests library automates and simplifies many of the tasks that we've been looking at.

"""

import requests

# submit a request
response = requests.get('http://www.debian.org')

# print the properties of the response object
print("[*] {}".format(response.status_code))
print("[*] {}".format(response.reason))
print("[*] {}".format(response.url))
print("[*] {}".format(response.headers['content-type']))

# Requests library convenience attributes of the response object
print("[*] {}".format(response.ok))
print("[*] {}".format(response.is_redirect))

# Access the request properties through the response object
print("[*] {}".format(response.request.headers))  # note how Requests lib auto handles compression for us

# show content encoding
print("[*] {}".format(response.headers['content-encoding']))

# show the bytes object (like HTTPResponse)
print("[*] {}".format(response.content))

# perform automatic decoding
print("[*] {}".format(response.text))  # notice this is a str(), not bytes()

# show what encoding 'Requests' has chosen one step back
print("[*] {}".format(response.encoding))

# decide yourself what coding 'Requests' should use
# print("[*] {}".format(response.encoding('utf-8')))

# 'Requests' automatically handles cookies
response = requests.get('http://www.github.com')
print("[*] {}".format(response.cookies))

# use 'Requests' Session class, which allows the reuse of cookies
# this is similar to using the http module's CookieJar and urllib's HTTPCookieHandler
"""
The Session object has the same interface as the requests module,
so we use its get() method in the same way as we use the requests.get() method.
Now, any cookies encountered are stored in the Session object,
and they will be sent with corresponding requests when we use the get() method in the future.
"""
s = requests.Session()
s.get('http://www.google.com')
response = s.get('http://google.com/preferences')

# redirects are also automatically followed, like urllib
# redirected requests are captured in the 'history' attribute

# different HTTP methods are accessible through their own functions
# response = requests.head('http://www.google.com')

# custom headers are added to the requests in a similar fashion as urllib
# headers = {'User-Agent': 'Mozilla/5.0 Firefox 24'}
# response = requests.get('http://www.debian.org', headers=headers)

# making requests with query strings is a straightforward process
params = {'action': 'search',  'term': 'Are you quite sure this is a cheese shop?'}
response = requests.get('http://pypi.python.org/pypi', params=params)
print("[*] {}".format(response.url))
