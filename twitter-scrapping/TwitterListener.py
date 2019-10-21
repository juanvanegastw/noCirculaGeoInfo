from tweepy.streaming import StreamListener
import json
import logging


class TwitterListener(StreamListener):
    def on_data(self, raw_data):
        data = json.loads(raw_data)
        text = data.get('text', '')
        user = data.get('user', {})
        name = user.get('name', '')
        logging.info('Text: ' + text)
        logging.info('User: ' + name)
        return True

    def on_error(self, status):
        logging.error(status)
        return True
