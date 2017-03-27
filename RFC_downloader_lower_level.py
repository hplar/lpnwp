#!/usr/bin/env python

"""
Page 87: Looking Deeper
Dealing with a raw HTTP protocol exchange.
"""

import sys
import socket


try:
    rfc_number = int(sys.argv[1])
except (IndexError, ValueError):
    print('Must supply an RFC number as first argument')
    sys.exit(2)

# define target
target_host = 'www.ietf.org'
target_port = 80

# socket.create_connection always connects with TCP
sock = socket.create_connection((target_host, target_port))

# HTTP request to be sent
req = (
    'GET /rfc/rfc{rfcnum}.txt HTTP/1.1\r\n'
    'Host: {host}:{port}\r\n'
    'User-Agent: Python {version}\r\n'
    'Connection: close\r\n'
    '\r\n'
)

# format the template with variables
req = req.format(
    rfcnum=rfc_number,
    host=target_host,
    port=target_port,
    version=sys.version_info[0],
)

# send the entire formatted request string as ascii
sock.sendall(req.encode('ascii'))

# declare data structure to hold incoming data
rfc_raw = bytearray()

# start loop
while True:
    # read data from socket
    buf = sock.recv(4096)
    # no more data, break from loop
    if not len(buf):
        break
    # add received data to bytearray
    rfc_raw += buf

# decode raw data (ascii) to utf-8
rfc = rfc_raw.decode('utf-8')

# print the result
print(rfc)
