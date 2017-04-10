#!/usr/bin/env python

"""

Chapter2: URL encoding
Page 152

----------------------

URLs are restricted to the ASCII characters and within this set,
a number of characters are reserved and need to be escaped in different components of a URL.
We escape them by using something called URL encoding.
It is often called percent encoding, because it uses the percent sign as an escape character.

The full rules for where the reserved characters need to be escaped are given in RFC 3986,
however urllib provides us with a couple of methods for helping us construct URLs.
This means that we don't need to memorize all of these!

We just need to:

1. URL-encode the path
2. URL-encode the query string


"""

from urllib.parse import quote, urlunparse, urlencode

# example url encoded string
result = quote('a duck?')
print("[*] {}".format(result))

# encode a path
path = 'pypi'
path_enc = quote(path)
# create a query dict
query_dict = {'action': 'search', 'term': 'Are you quite sure this is a cheese shop?'}
# encode the query dict
query_enc = urlencode(query_dict)
print("[*] {}".format(query_enc))  # preview the encoded path + query
# compose everything into an url
netloc = 'pypi.python.org'
result = urlunparse(('http', netloc, path_enc, '', query_enc, ''))
print("[*] {}".format(result))


# the quote() function has been setup for specifically encoding paths.
# by default, it ignores slashes and it doesn't encode them
path = '/images/users/+Zoot+/'
print("[*] {}".format(quote(path)))


# when there is a slash in the elements of a path, we run into trouble
# the slash is interpreted as a dir level
username = '+Zoot/Dingo+'
path = 'images/users/{}'.format(username)
print("[*] {}".format(quote(path)))

# to fix the above, we need to escape any path elements that may contain slashes first
# then join them manually
username = '+Zoot/Dingo+'
user_encoded = quote(username, safe='')
path = '/'.join(('', 'images', 'users', user_encoded))
print("[*] {}".format(path))
