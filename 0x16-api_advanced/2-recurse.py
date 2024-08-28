#!/usr/bin/python3
"""
Recursively queries Reddit API and returns a list containing the titles
"""

import json
import requests


def recurse(subreddit, hot_list=[], after=None):
    """
    returns a list containing the titles of all hot articles
    for a given subreddit
    """
    if hot_list is None:
        hot_list = []
    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=100"
    if after:
        url += f"&after={after}"
    headers = {"User-Agent": "Python/requests"}
    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code != 200:
        return None
    try:
        data = response.json()
        posts = data['data']['children']
    except KeyError:
        return None
    if not posts:
        return hot_list
    for post in posts:
        hot_list.append(post['data']['title'])
    after = data['data']['after']
    return recurse(subreddit, hot_list, after)
