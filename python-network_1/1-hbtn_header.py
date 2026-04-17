#!/usr/bin/python3
"""
This script takes in a URL, sends a request and displays the value
of the X-Request-Id variable found in the header of the response.
"""
import urllib.request
import sys


if __name__ == "__main__":
    url = sys.argv[1]
    # Firewall bypass üçün başlıq əlavə edirik
    headers = {'cfclearance': 'true'}
    req = urllib.request.Request(url, headers=headers)

    with urllib.request.urlopen(req) as response:
        # get() metodu istifadə edilməlidir (tələblərə əsasən)
        request_id = response.headers.get('X-Request-Id')
        print(request_id)
