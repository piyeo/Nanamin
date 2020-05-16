# -*- coding: utf-8 -*-
import tweepy
import key
import omake
import random
#from requests_oauthlib import OAuth1Session

auth = tweepy.OAuthHandler(key.CK, key.CS)
auth.set_access_token(key.AT, key.AS)

api = tweepy.API(auth)

Twitter_ID = str(api.me().screen_name)

timeline = api.mentions_timeline(count=1)

for status in timeline:
    status_id = status.id
    screen_name = status.user.screen_name
    text = str(status.text).replace("\n", "")
    f = ""
    if not status.favorited:
        res = ""
        if "おまけ集め" in text:
            day = status.created_at.day
            if status.created_at.hour + 9 >= 24:
                day += 1
            cmd = ""
            if "リセット" in text and "リスト" not in text:
                cmd = "reset"
            elif "リスト" in text:
                cmd = "list"
            res = omake.collect(day, screen_name, cmd)
        elif "普通じゃ" in text or "異常" in text or "普通なの" in text or "普通か？" in text or "普通とは" in text or\
                "変" in text:
            f = open("texts/ijou.txt", "r")
        elif "普通" in text or "変じゃ":
            f = open("texts/futuu.txt", "r")
        else:
            f = open("texts/response.txt", "r")
        if f:
            line = f.readlines()
        if not res:
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


