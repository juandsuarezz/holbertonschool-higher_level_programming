#!/usr/bin/python3
"""
Takes in a URL and email and sends a POST request to URL with email
as a parameter, then displays the response
"""

import urllib.request
import urllib.parse
from sys import argv

if __name__ == '__main__':
    url = argv[1]
    email = argv[2]

    data = urllib.parse.urlencode({'email': email})
    data = data.encode('ascii')
    request = urllib.request.Request(url, data)
    with urllib.request.urlopen(request) as response:
        html = response.read()
        utf = html.decode('utf-8')
    print(utf)
