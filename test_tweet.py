import tweepy
import datetime
import pytz
import random
import key
import omake

auth = tweepy.OAuthHandler(key.CK, key.CS)
auth.set_access_token(key.AT, key.AS)

api = tweepy.API(auth)

Twitter_ID = str(api.me().screen_name)

api.update_status("全部壁がもろいのがいけないんって普通だよね……？というわけで、おやすみなさ〜い")