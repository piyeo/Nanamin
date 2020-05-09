#-*- coding:utf-8 -*-
import tweepy
import key
import random

auth = tweepy.OAuthHandler(key.CK, key.CS)
auth.set_access_token(key.AT, key.AS)
api = tweepy.API(auth)

Twitter_ID = "hiromachinanami"

f = open("texts/response.txt", "r")
l = f.readlines()
response = "".join(random.sample(l,1))


class MyStreamListener(tweepy.StreamListener):
    def on_status(self, status):
        status_id = status.id
        screen_name = status.user.screen_name
        if str(status.in_reply_to_screen_name) == Twitter_ID:
            res = response
            if "Name" in res:
                res = res.replace("Name", str(status.user.name))
            reply_text = "@" + screen_name + " " + res + "　" * random.randint(0,5)
            api.create_favorite(status_id)
            if str(screen_name) != Twitter_ID:
                api.update_status(status=reply_text, in_reply_to_status_id=status_id)
            else:
                print("自分に返信送っちゃだめ")


stream = tweepy.Stream(auth, MyStreamListener())
while True:
    try:
        stream.filter(track=["@hiromachinanami"])
    except KeyboardInterrupt:
        stream.disconnect()
        break
    except Exception as e:
        stream.disconnect()
        print(e)