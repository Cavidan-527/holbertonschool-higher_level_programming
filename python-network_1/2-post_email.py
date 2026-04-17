#!/usr/bin/python3
"""
This script takes in a URL and an email, sends a POST request to the
passed URL with the email as a parameter, and displays the body.
"""
import urllib.request
import urllib.parse
import sys


if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]
    
    # POST məlumatını hazırlayırıq
    values = {'email': email}
    data = urllib.parse.urlencode(values)
    data = data.encode('ascii')  # Məlumat bayt formatında olmalıdır
    
    # Firewall bypass üçün başlıq əlavə edirik
    headers = {'cfclearance': 'true'}
    req = urllib.request.Request(url, data=data, headers=headers)

    with urllib.request.urlopen(req) as response:
        body = response.read()
        print(body.decode('utf-8'))
