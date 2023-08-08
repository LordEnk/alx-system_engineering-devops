#!/usr/bin/python3
"""Module for top_ten subreddit"""
import requests

def top_ten(subreddit):
    """Queries the Reddit API and returns the top 10 hot posts
    of the subreddit"""

    response = requests.get("https://www.reddit.com/r/{}/hot.json?limit=10"
                            .format(subreddit),
                            headers={"User-Agent": "My-User-Agent"},
                            allow_redirects=False)
    if response.status_code == 200:
        data = response.json().get('data', {}).get('children', [])
        for i, post in enumerate(data):
            print(f"{i+1}. {post['data']['title']}")
    else:
        print("None")
