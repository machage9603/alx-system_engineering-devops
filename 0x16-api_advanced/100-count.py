#!/usr/bin/python3
"""
Recursively queries Reddit API, parses the title of all hot articles and prints
"""

import json
import requests


def count_words(subreddit, word_list, after=None, count_dict=None):
    """
    parses the title of all hot articles, and prints a sorted count
    of given keywords (case-insensitive, delimited by spaces.
    Javascript should count as javascript, but java should not).
    """
    if count_dict is None:
        count_dict = {}
    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=100"
    if after:
        url += f"&after={after}"
    headers = {"User-Agent": "Python/requests"}
    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code != 200:
        return
    data = response.json()
    posts = data.get('data', {}).get('children', [])
    for post in posts:
        title = post.get('data', {}).get('title', '').lower()
        for word in word_list:
            if word.lower() in title:
                count_words = count_dict.get(word, 0)
                count_title = title.count(word.lower())
                count_dict[word] = count_words + count_title
    after = data['data']['after']
    if after:
        return count_words(subreddit, word_list, after, count_dict)
    else:
        sorted_counts = sorted(count_dict.items(), key=lambda x: (-x[1], x[0]))
        for word, count in sorted_counts:
            print(f"{word}: {count}")
