#!/usr/bin/python3
"""
a function that queries the Reddit API and returns the
number of subscribers for a given subreddit.
If an invalid subreddit is given, the function should return 0
"""
import requests

def number_of_subscribers(subreddit):
    """
    a function that queries the Reddit API and returns the
    number of subscribers for a given subreddit.
    If an invalid subreddit is given, the function should return 0
    """
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {"User-Agent": "app"}

    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        if response.status_code == 200:
            data = response.json()
            return data['data']['subscribers']
        else:
            return 0
    except requests.exceptions.RequestException:
        return 0
