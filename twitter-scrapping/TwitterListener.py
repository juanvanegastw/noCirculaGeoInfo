from tweepy.streaming import StreamListener
import json


class TwitterListener(StreamListener):
    def on_data(self, raw_data):
        data = json.loads(raw_data)
        text = data.get('text', '')
        user = data.get('user', {})
        name = user.get('name', '')
        print(text)
        print('User: ', name)
        return True

    def on_error(self, status):
        print(status)
        return True
