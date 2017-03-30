#!/usr/bin/env python

"""
Chapter 2: Cookies
Page 136

---
A cookie is a small piece of data that the server sends in a Set-Cookie header as a part of the response.
The client stores cookies locally and includes them in any future requests that are sent to the server.

"""

from http.cookiejar import CookieJar
from urllib.request import build_opener, HTTPCookieProcessor
import datetime

# create an object to store cookies
cookie_jar = CookieJar()

# create an urllib opener, it will extract cookies from the responses we receive and store them in the cookiejar
opener = build_opener(HTTPCookieProcessor(cookie_jar))

# use our opener to make an HTTP request
opener.open('http://www.github.com')

# check that the server has sent us cookies
print("[*] {}".format(len(cookie_jar)))

"""
The http.cookiejar module also contains a FileCookieJar class, that works in the same way as CookieJar, but
it provides an additional function for easily saving the cookies to a file.
This allows persistence of cookies across Python sessions.
"""

# check the cookies in the cookiejar
cookies = list(cookie_jar)
for cookie in cookies:
    print("[*] {}".format(cookie))

# extract information from the first cookie
print("[*] {}".format(cookies[0].name))     # name allows server to reference it
print("[*] {}".format(cookies[0].value))
print("[*] {}".format(cookies[0].domain))   # area for which this cookie is valid
print("[*] {}".format(cookies[0].path))     # area for which this cookie is valid
print("[*] {}".format(cookies[0].expires))  # unix timestamp -> use datetime module to convert

# convert unix timestamp to datetiome
print("[*] {}".format(datetime.datetime.fromtimestamp(cookies[0].expires)))

# a common cookie flag
print("[*] {}".format(cookies[0].get_nonstandard_attr('HttpOnly')))

# another common cookie flag
print("[*] {}".format(cookies[0].secure))
