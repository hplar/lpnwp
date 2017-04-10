#!/usr/bin/env python

"""
Chapter 2: Requests with urllib
Pages: 108 - 112
"""

from urllib.request import urlopen


# send a request and receive a response
response = urlopen('http://www.debian.org')

# show the HTTPResponse object
print("[*] {}".format(response))

# read a line from the HTTPResponse object
print("[*] {}".format(response.readline()))

# view the REQUEST source for the response object
print("[*] {} ".format(response.url))

# use read() to access the response object's file-like interface (takes int n number of bytes to read)
print("[*] {} ".format(response.read(50)))

# read the response status
print("[*] {} ".format(response.status))
