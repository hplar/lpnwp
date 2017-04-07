#!/usr/bin/env python

"""
Chapter 2: Query Strings
Page: 149 -
------------------------

RFC 3986 defines another property of URLs.
They can contain additional parameters in the form of key/value pairs that appear after the path.
They are separated from the path by a question mark, as shown here:

http://docs.python.org/3/search.html?q=urlparse&area=default

This string of parameters is called a query string. Multiple parameters are separated by ampersands (&).

"""

from urllib.request import urlopen, urlparse
from urllib.parse import parse_qs

# example of parsing query strings with urllib urlparse
result = urlparse('http://docs.python.org/3/search.html?q=urlparse&area=default')
print("[*] {}".format(result))

# use urllib.parse to turn the query component returned by urlparse into a dict
parsed_queries = parse_qs(result.query)
print("[*] {}".format(parsed_queries))

# the dict values are lists because parameters can appear more than once in a query string
result = urlparse('http://docs.python.org/3/search.html?q=urlparse&q=urljoin')
parsed_queries = parse_qs(result.query)
print("[*] {}".format(parsed_queries))
