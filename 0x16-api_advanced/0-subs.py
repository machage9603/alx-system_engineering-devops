#!/usr/bin/python3
"""This module queries Reddit API and returns the number of subscribers"""

import json
import requests


def number_of_subscribers(subreddit):
    """Returns the total number of subscribers"""
    # check if subreddit is valid
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    # set headers
    headers = {"User-Agent": "Python/requests"}
    # make request
    response = requests.get(url, headers=headers, allow_redirects=False)
    #check id status code is Ok
    if response.status_code == 200:
        # if status code is 200, return number of subscribers
        data = response.json()
        return data['data']['subscribers']
    else:
        # if status code is not 200, return 0
        return 0
