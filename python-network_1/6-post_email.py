#!/usr/bin/python3
"""
This script takes in a URL and an email address, sends a POST request
to the passed URL with the email as a parameter, and displays the body.
"""
import requests
import sys


if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]
    payload = {'email': email}
    # Firewall bypass başlığı əlavə edilir
    headers = {'cfclearance': 'true'}
    response = requests.post(url, data=payload, headers=headers)
    print(response.text)
