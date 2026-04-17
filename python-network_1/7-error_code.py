#!/usr/bin/python3
"""
This script takes in a URL, sends a request to the URL and displays
the body of the response. It handles HTTP errors (>= 400).
"""
import requests
import sys


if __name__ == "__main__":
    url = sys.argv[1]
    # Firewall bypass üçün başlıq əlavə olunur
    headers = {'cfclearance': 'true'}
    response = requests.get(url, headers=headers)
    # Status kodu 400 və ya daha böyükdürsə xəta çap olunur
    if response.status_code >= 400:
        print("Error code: {}".format(response.status_code))
    else:
        print(response.text)
