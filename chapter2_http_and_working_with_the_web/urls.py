#!/usr/bin/env python

"""
Chapter 2: URLs (paths & relative urls)
Page 146
"""

from urllib.parse import urlparse, urljoin

result = urlparse('http://www.python.org/dev/peps')
print("[*] {}".format(result))

# print only the network location
print("[*] {}".format(result.netloc))

# print only the path at the network location
print("[*] {}".format(result.path))

# manually add a port number (default http: 80, default https: 443)
result = urlparse('http://www.python.nl:8080/')
print("[*] {}".format(result))

# example of an absolute URL (scheme and host are supplied, see results)
result = urlparse('http://www.python.org/')
print("[*] {}".format(result))

# example of a relative URL (no scheme, no host)
result = urlparse('../images/tux.png')
print("[*] {}".format(result))

# join a relative and absolute url together to one absolute url
result = urljoin('http://www.debian.org', 'intro/about')
print("[*] {}".format(result))
print("[*] {}".format(result))

# The only time that urljoin will fill in a slash for us
# is when the base URL does not have a path,
result = urljoin('http://www.debian.org/intro/', 'about')
result2 = urljoin('http://www.debian.org/intro', 'about')  # this will replace /intro with /about
print("[*] {}\n[*] {}".format(result, result2))

# force replacement of all the elements of a base url by prefixing it with a slash
result = urljoin('http://www.debian.org/intro/about', '/News')
print("[*] {}".format(result))

# navigating to parent directories
result = urljoin('http://www.debian.org/intro/about/', '../News')
result2 = urljoin('http://www.debian.org/intro/about/', '../../News')
result3 = urljoin('http://www.debian.org/intro/about', '../News')
print("[*] {}\n[*] {}\n[*] {}".format(result, result2, result3))

# when the 'relative url' is actually an absolute url
result = urljoin('http://www.debian.org', 'http://www.python.org')  # it replaces the base url
print("[*] {}".format(result))
