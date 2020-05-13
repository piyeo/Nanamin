import tweepy
import random
import datetime
import pytz

import key

auth = tweepy.OAuthHandler(key.CK, key.CS)
auth.set_access_token(key.AT, key.AS)

api = tweepy.API(auth)

times = [10, 12, 14, 16, 18, 20, 22]

dt_now = datetime.datetime.now(pytz.timezone('Asia/Tokyo'))

f = open("texts/simple.txt", "r")
l = f.readlines()
s = random.sample(l,1)
print("".join(s))

for time in times:
    if dt_now.hour == time:
        api.update_status("".join(s))
        break

