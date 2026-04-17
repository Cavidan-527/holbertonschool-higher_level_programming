#!/usr/bin/python3
"""
This module contains functions to interact with a public API,
process JSON data, and save it into a CSV file.
"""
import requests
import csv


def fetch_and_print_posts():
    """
    Fetches all posts from JSONPlaceholder and prints their titles.
    """
    url = "https://jsonplaceholder.typicode.com/posts"
    r = requests.get(url)

    print("Status Code: {}".format(r.status_code))

    if r.status_code == 200:
        posts = r.json()
        for post in posts:
            print(post.get('title'))


def fetch_and_save_posts():
    """
    Fetches all posts and saves them into a CSV file named posts.csv.
    """
    url = "https://jsonplaceholder.typicode.com/posts"
    r = requests.get(url)

    if r.status_code == 200:
        posts = r.json()
        # Məlumatı lüğətlər siyahısı (list of dictionaries) şəklində hazırlayırıq
        data_to_save = []
        for post in posts:
            data_to_save.append({
                'id': post.get('id'),
                'title': post.get('title'),
                'body': post.get('body')
            })

        # CSV faylına yazma hissəsi
        with open('posts.csv', mode='w', encoding='utf-8', newline='') as f:
            fieldnames = ['id', 'title', 'body']
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(data_to_save)
