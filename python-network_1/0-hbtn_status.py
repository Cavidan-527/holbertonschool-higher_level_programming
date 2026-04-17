#!/usr/bin/python3
"""
This script fetches https://intranet.hbtn.io/status using urllib.
It demonstrates how to handle HTTP responses and display content types.
"""
import urllib.request


if __name__ == "__main__":
    url = "https://intranet.hbtn.io/status"
    with urllib.request.urlopen(url) as response:
        content = response.read()
        print("Body response:")
        print("\t- type: {}".format(type(content)))
        print("\t- content: {}".format(content))
        print("\t- utf8 content: {}".format(content.decode('utf-8')))
