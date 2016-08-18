#!/usr/bin/python2.7 -tt

import sys
import os
import time
import urllib
import requests
from requests_oauthlib import OAuth1

CONSUMER_KEY = os.getenv('CONSUMER_KEY', 'rvyCmF9B8X348O0yzLCMADEHQ')
CONSUMER_SECRET = os.getenv('CONSUMER_SECRET', 'NJeTfA6vIny7c2y4b9Jl38cPSQGbLhGCwAhXNt1fGCHscHAcrp')
ACCESS_TOKEN_KEY = os.getenv('ACCESS_TOKEN_KEY', '193453505-7jVDGjIoTKcbHytGAB73nJZugdVuzFIgzJEiYI1M')
ACCESS_TOKEN_SECRET = os.getenv('ACCESS_TOKEN_SECRET', 'oDy27ogsMOnZG5VlYHqHteoTpSXAMotXQ7NiajbQ2bvCx')

def main():
    print "hello"
    # url = 'https://api.twitter.com/1.1/account/verify_credentials.json'
    url = 'https://api.twitter.com/1.1/statuses/home_timeline.json'
    payload = {'count': '1'}
    auth = OAuth1(CONSUMER_KEY, CONSUMER_SECRET,
                  ACCESS_TOKEN_KEY, ACCESS_TOKEN_SECRET)
    r = requests.get(url, auth=auth, params=payload)
    print r.json()

# Boilerplate
if __name__ == '__main__':
    main()

