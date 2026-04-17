#!/usr/bin/python3
"""
This script takes in a URL, sends a request to the URL and displays
the body of the response (decoded in utf-8).
It handles HTTP errors by printing the error code.
"""
import urllib.request
import urllib.error
import sys


if __name__ == "__main__":
    url = sys.argv[1]
    # Firewall bypass başlığını daxil edirik
    headers = {'cfclearance': 'true'}
    req = urllib.request.Request(url, headers=headers)

    try:
        with urllib.request.urlopen(req) as response:
            print(response.read().decode('utf-8'))
    except urllib.error.HTTPError as e:
        print("Error code: {}".format(e.code))
