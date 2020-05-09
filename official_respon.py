import tweepy
import random

import key

auth = tweepy.OAuthHandler(key.CK, key.CS)
auth.set_access_token(key.AT, key.AS)

api = tweepy.API(auth)

timeline = api.user_timeline(screen_name="bang_dream_gbp", count=3)

for status in timeline:
    status_id = status.id
    screen_name = status.author.screen_name
    sentence = str(status.text).replace('\n', '')
    if "七深" in sentence:
        api.create_favorite(status_id)
        api.retweet(status.id)
        reply_text = "@" + screen_name + " " + "広町はっけーーん！"
        api.update_status(status=reply_text, in_reply_to_status_id=status_id)