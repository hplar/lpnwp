#!/usr/bin/env python

"""

Chapter 2: Content negotiation
Page 128 - 132

----

Content compression with the Accept-Encoding header and language selection with
the Accept-Language header are examples of content negotiation,
where the client specifies its preferences regarding the format and the content of
the requested resource. The following headers can also be used for this:

Accept: For requesting a preferred file format
Accept-Charset: For requesting the resource in a preferred character set

"""

from urllib.request import urlopen

# check Content-Type header for www.debian.org
response = urlopen('http://www.debian.org')
print("[*] {}".format(response.getheader('Content-Type')))


# submit request for www.python.org
response = urlopen('http://www.python.org')

# check the Content-Type and extract the character set
data_format, params = response.getheader('Content-Type').split(';')
print("[*] {}".format(params))
charset = params.split('=')[1]
print("[*] {}".format(charset))

# decode our response content by using the supplied character set
content = response.read().decode(charset)
print("[*] {}".format(content))
