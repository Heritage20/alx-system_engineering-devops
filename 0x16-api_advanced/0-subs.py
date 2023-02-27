#!/usr/bin/python3
# Finds total subscribers to a subreddit
import requests


def number_of_subscribers(subreddit):
    '''Function that returns total subscriber number'''
    URL = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
    USER_AGENT = {'User-Agent':
                 'Unix:com.holberton.apiadvanced:task0 (by /u/_marc_marc_)'}
    req = requests.get(URL, headers=USER_AGENT)
    if req.status_code is not 200:
        return (0)
    jreq = req.json()
    return (jreq['data']['subscribers'])
