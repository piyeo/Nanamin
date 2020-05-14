import tweepy
import random

import key

auth = tweepy.OAuthHandler(key.CK, key.CS)
auth.set_access_token(key.AT, key.AS)

api = tweepy.API(auth)

times = [10, 12, 14, 15, 17, 18, 19, 20, 21, 22, 23]

f = open("texts/simple.txt", "r")
l = f.readlines()
s = random.sample(l,1)
print("".join(s))

api.update_status("".join(s))

