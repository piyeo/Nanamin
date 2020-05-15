#-*- coding:utf-8 -*-
import tweepy
import key
import random

auth = tweepy.OAuthHandler(key.CK, key.CS)
auth.set_access_token(key.AT, key.AS)
api = tweepy.API(auth)

Twitter_ID = str(api.me().screen_name)
filter_ID = "@" + Twitter_ID

class MyStreamListener(tweepy.StreamListener):
    def on_status(self, status):
        status_id = status.id
        screen_name = status.user.screen_name
        text = str(status.text).replace("\n", "")
        f = ""
        if str(status.in_reply_to_screen_name) == Twitter_ID:
            if "普通じゃ" in text or "異常" in text or "普通なの" in text or "普通か？" in text or "普通とは" in text or\
                    "変" in text:
                f = open("texts/ijou.txt", "r")
            elif "普通" in text or "変じゃ":
                f = open("texts/futuu.txt", "r")
            else:
                f = open("texts/response.txt", "r")
            line = f.readlines()
            res = "".join(random.sample(line, 1))
            if "Name" in res:
                res = res.replace("Name", str(status.user.name))
            reply_text = "@" + screen_name + " " + res + "　" * random.randint(0, 5)
            api.create_favorite(status_id)
            if str(screen_name) != Twitter_ID:
                api.update_status(status=reply_text, in_reply_to_status_id=status_id)
            else:
                print("自分に返信送っちゃだめ")


stream = tweepy.Stream(auth, MyStreamListener())
while True:
    try:
        stream.filter(track=[filter_ID])
    except KeyboardInterrupt:
        stream.disconnect()
        break
    except Exception as e:
        stream.disconnect()
        print(e)