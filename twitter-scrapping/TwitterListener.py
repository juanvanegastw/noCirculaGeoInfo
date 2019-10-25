from tweepy.streaming import StreamListener
import json
import logging


class TwitterListener(StreamListener):
    def __init__(self, producer, twitter_track):
        super().__init__()
        self.producer = producer
        self.twitter_track = twitter_track

    def on_data(self, raw_data):
        data = json.loads(raw_data)
        text = data.get('text', '')
        user = data.get('user', {})
        name = user.get('name', '')
        logging.info('Text: ' + text)
        logging.info('User: ' + name)
        message = {'user': name, 'text': text}
        self.producer.send(self.twitter_track, message)
        return True

    def on_error(self, status):
        logging.error(status)
        return True
