#!/usr/bin/python3
"""
This script takes in a URL, sends a request to the URL and displays
the value of the variable X-Request-Id in the response header.
"""
import requests
import sys


if __name__ == "__main__":
    url = sys.argv[1]
    # Firewall-u keçmək üçün başlıq mütləqdir
    headers = {'cfclearance': 'true'}
    
    response = requests.get(url, headers=headers)
    # requests kitabxanasında başlıqları .headers.get() ilə çəkirik
    request_id = response.headers.get('X-Request-Id')
    
    if request_id:
        print(request_id)
