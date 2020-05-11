import tweepy
import random

import key

auth = tweepy.OAuthHandler(key.CK, key.CS)
auth.set_access_token(key.AT, key.AS)

api = tweepy.API(auth)

api.update_status("今から運動してきますだいたい5キロか6キロくらい走るのって普通……だよね？")