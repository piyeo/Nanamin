# -*- coding: utf-8 -*-
import tweepy
import key
import random
#from requests_oauthlib import OAuth1Session

auth = tweepy.OAuthHandler(key.CK, key.CS)
auth.set_access_token(key.AT, key.AS)

api = tweepy.API(auth)

Twitter_ID = str(api.me().screen_name)

timeline = api.mentions_timeline()

for status in timeline:
    status_id = status.id
    screen_name = status.author.screen_name
    if not status.favorited:
        f = open("texts/response.txt", "r")
        line = f.readlines()
        res = "".join(random.sample(line, 1))
        if "Name" in res:
            res = res.replace("Name", str(status.user.name))
        try:
            reply_text = "@" + screen_name + " " + res
            api.create_favorite(status.id)
            if str(status.in_reply_to_screen_name) == Twitter_ID and str(status.user.screen_name) != Twitter_ID:
                api.update_status(status=reply_text, in_reply_to_status_id=status_id)
            else:
                print("自分に返信送っちゃだめ")
        except:
            print("すでに返信してるよー")


