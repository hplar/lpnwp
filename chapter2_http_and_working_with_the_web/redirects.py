#!/usr/bin/env python

"""
Chapter 2: Redirects
Page 143

---

The 300 range of HTTP status codes is designed for this purpose.
These codes indicate to the client that further action is required on their part to complete the request.
 The most commonly encountered action is to retry the request at a different URL. This is called a redirect.

"""

from urllib.request import Request, urlopen


# submit request for www.gmail.com
req = Request('http://www.gmail.com')
response = urlopen(req)

# notice that we have been redirected to the google login page
print("[*] {}".format(response.url))

# print the request redirection dictionary()
print("[*] {}".format(req.redirect_dict))
