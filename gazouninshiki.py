#-*- coding:utf-8 -*-
import tweepy
import key

auth = tweepy.OAuthHandler(key.CK, key.CS)
auth.set_access_token(key.AT, key.AS)
api = tweepy.API(auth)

Twitter_ID = str(api.me().screen_name)
filter_ID = "@" + Twitter_ID


class MyStreamListener(tweepy.StreamListener):
    def on_status(self, status):
        entities = status.entities
        if "media" in entities:
            media = entities["media"]
            print(media[0]['media_url'])

stream = tweepy.Stream(auth, MyStreamListener())
while True:
    try:
        stream.filter(track=["nyabekonyabeko"])
    except KeyboardInterrupt:
        stream.disconnect()
        break
    except Exception as e:
        stream.disconnect()
        print(e)