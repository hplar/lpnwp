#!/usr/bin/env python

from urllib.request import urlopen


url = input(str("URL: "))
response = urlopen("http://{}".format(url))

target_file = "./downloads/{}.html".format(url)

with open(target_file, 'w') as f:
    print("opening file and starting write")
    line = response.readline().decode()
    while True:
        f.write(line)
        line = response.readline().decode()
        if line == "":
            print("no more lines -> exit.")
            exit()
