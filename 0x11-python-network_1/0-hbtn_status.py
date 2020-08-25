#!/usr/bin/python3
"""
Fetches the following link: https://intranet.hbtn.io/status
"""

import urllib.request

if __name__ == '__main__':
    with urllib.request.urlopen('https://intranet.hbtn.io/status') as response:
        html = response.read()
        utf8_format = html.decode('utf-8')

    print("Body response:")
    print("\t- type: {}".format(type(html)))
    print("\t- content: {}".format(html))
    print("\t- utf8 content: {}".format(utf8_format))
