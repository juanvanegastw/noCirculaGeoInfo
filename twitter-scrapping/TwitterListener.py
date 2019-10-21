from tweepy.streaming import StreamListener
import json
import logging

logging.basicConfig(filename='twitter.log', filemode='w', format='%(name)s - %(levelname)s - %(message)s')


class TwitterListener(StreamListener):
    def on_data(self, raw_data):
        data = json.loads(raw_data)
        text = data.get('text', '')
        user = data.get('user', {})
        name = user.get('name', '')
        logging.warning('Text', text)
        logging.warning('User', name)
        return True

    def on_error(self, status):
        logging.error(status)
        return True
