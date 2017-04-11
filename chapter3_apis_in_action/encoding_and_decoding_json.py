#!/usr/bin/env python

"""

Chapter 3: JSON
Page: 221

---------------

JavaScript Object Notation (JSON) is a standard way of representing simple objects,
such as lists and dicts, in the form of text strings.
Although, it was originally developed for JavaScript,
JSON is language independent and most languages can work with it.
It's lightweight, yet flexible enough to handle a broad range of data.
This makes it ideal for exchanging data over HTTP,
and a large number of web APIs use this as their primary data format.

"""

import json

# create a list first
l = ['a', 'b', 'c']
# convert the list object to a json string
print(json.dumps(l))
# verify that it's really a string
s = json.dumps(l)
print(type(s))

# a json string
s = '["a", "b", "c"]'
# convert to python object (list)
l = json.loads(s)
print(l)
# verify it's a list
print(type(l))

# dicts and json maps
d = {
    'Chapman': ['King Arthur', 'Brian'],
    'Cleese': ['Sir Lancelot', 'The Black Knight'],
    'Idle': ['Sir Robin', 'Loretta'],
    }
print(json.dumps(d))

# json dictionary keys can ONLY be in the form strings
print(json.dumps({1: 10, 2: 20, 3: 30}))  # keys with ints as values will get converted

# to get ints as keys in dicts, we have to manually convert them
j = json.dumps({1: 10, 2: 20, 3: 30})
d_raw = json.loads(j)
# use a dictionary comprehension to apply int() to the dict keys
print({int(key): val for key, val in d_raw.items()})

# json doesn't implement tuples -> they will become lists
t = ('a', 'b', 'c')
j = json.dumps(t)
print(json.loads(j))

# json doesn't implement sets -> they need to be converted to lists
s = set([1, 2, 3])
# wrong = json.dumps(s)  # returns a TypeError
right = json.dumps(list(s))
print(type(right))
