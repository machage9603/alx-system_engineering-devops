#!/usr/bin/python3
"""Queries Reddit API and prints the titles of the first 10 hot posts listed"""


import json
import requests


def top_ten(subreddit):
    """
    Prints the titles of the first 10 hot posts listed for a given subreddit
    """
    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=10"
    headers = {"User-Agent": "Python/requests"}
    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code != 200:
        print(None)
        return
    data = response.json()
    if 'error' in data:
        print(None)
        return
    posts = data['data']['children']
    for post in posts:
        print(post['data']['title'])
