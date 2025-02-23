#-*- coding:utf-8 -*-
import tweepy
import key
import random

auth = tweepy.OAuthHandler(key.CK, key.CS)
auth.set_access_token(key.AT, key.AS)

api = tweepy.API(auth)

Twitter_ID = str(api.me().screen_name)


class MyStreamListener(tweepy.StreamListener):
    def on_status(self, status):
        status_id = status.id
        screen_name = status.user.screen_name
        if str(screen_name) == "bang_dream_gbp":
            if "七深" in str(status.text):
                api.create_favorite(status_id)
                api.retweet(status_id)
                if "紹介" in str(status.text) or ("イベント" in str(status.text) and "開催" in str(status.text)):
                    reply_text = "@" + screen_name + "  広町はっけーん！" + "　" * random.randint(0, 5)
                    api.update_status(status=reply_text, in_reply_to_status_id=status_id)


stream = tweepy.Stream(auth, MyStreamListener())
while True:
    try:
        stream.filter(track=["#バンドリ","#ガルパ"])
    except KeyboardInterrupt:
        stream.disconnect()
        break
    except Exception as e:
        stream.disconnect()
        print(e)

