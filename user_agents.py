#!/usr/bin/env python

"""
Chapter 2: User Agents
Page 133

---

Any client that communicates using HTTP can be referred to as a user agent.
RFC 7231 suggests that user agents should use the User-Agent header to identify themselves in every request.
What goes in there is up to the software that makes the request,
though it usually comprises a string that identifies the program and version,
and possibly the operating system and the hardware that it's running on.

"""

from urllib.request import Request, urlopen


# view the user-agent that urllib uses
req = Request('http://www.python.org')

# submit the request
response = urlopen(req)

# check the User-agent header that urlopen added
print("[*] {}".format(req.get_header('User-agent')))

# spoofing the User-Agent
req = Request('http://www.python.org')
req.add_header('User-Agent', 'Mozilla/5.0 (X11; Linux x86_64;rv:240) Gecko/20140722 Firefox/24.0 Iceweasel/24.7.0')
res = urlopen(req)
print("[*] {}".format(res.getheaders()))
