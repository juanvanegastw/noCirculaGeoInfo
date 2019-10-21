import os
import tweepy
from tweepy import OAuthHandler
from tweepy import Stream
from TwitterListener import TwitterListener
import logging

logging.basicConfig(filename='twitter.log',
                    format='%(asctime)s %(name)-12s %(levelname)-8s %(message)s',
                    filemode='w',
                    level=logging.INFO)


CONSUMER_KEY = os.environ.get('CONSUMER_KEY')
CONSUMER_SECRET = os.environ.get('CONSUMER_SECRET')
ACCESS_TOKEN = os.environ.get('ACCESS_TOKEN')
ACCESS_SECRET = os.environ.get('ACCESS_SECRET')
FOLLOWED_USER = os.environ.get('FOLLOWED_USER')
TWITTER_TRACK = os.environ.get('TWITTER_TRACK')

auth = OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)

api = tweepy.API(auth)

if __name__ == '__main__':
    logging.info('Twitter track' + TWITTER_TRACK)
    logging.info('User' + FOLLOWED_USER)
    FOLLOWED_USER = str(FOLLOWED_USER) if FOLLOWED_USER else ''
    TWITTER_TRACK = str(TWITTER_TRACK) if TWITTER_TRACK else ''
    twitter_stream = Stream(auth, TwitterListener())
    twitter_stream.filter(follow=[FOLLOWED_USER], track=[TWITTER_TRACK,])
