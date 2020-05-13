import tweepy
import random

import key

auth = tweepy.OAuthHandler(key.CK, key.CS)
auth.set_access_token(key.AT, key.AS)

api = tweepy.API(auth)

f = open("texts/simple.txt", "r")
l = f.readlines()
s = random.sample(l,1)
print("".join(s))

api.update_status("".join(s))

