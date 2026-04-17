#!/usr/bin/python3
"""
This script takes GitHub credentials (username and personal access token)
and uses the GitHub API to display the user's id.
"""
import requests
import sys


if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    url = "https://api.github.com/user"
    # Basic Authentication: (istifadəçi_adı, token)
    auth = (username, password)
    headers = {'cfclearance': 'true'}
    response = requests.get(url, auth=auth, headers=headers)
    try:
        json_res = response.json()
        print(json_res.get('id'))
    except ValueError:
        print("None")
