#!/usr/bin/python3
"""Module for the recursive reddit api"""
import requests


def recurse(subreddit, hot_list=[], count=0, after=None):
    """Queries the Reddit API and returns all hot posts
    of the subreddit"""

    response = requests.get("https://www.reddit.com/r/{}/hot.json"
                            .format(subreddit),
                            params={"count": count, "after": after},
                            headers={"User-Agent": "My-User-Agent"},
                            allow_redirects=False)
    if response.status_code == 200:
      data = response.json().get('data', {}.get('children', [])
      if not data:
        return hot_list

      for post in data:
        hot_list.append(post['data']['title'])

      after = data[-1]['data']['name']
      return recurese(subreddit, hot_list, after=after)

    elif response.status_code == 404:
      return None
