import tweepy
import random

import tokenizer

CK = "DKbyGy2z282qmy9A21h5xIf6Q"
CS = "HSQSGw8Om2zmtBF2hQxrJzjlZ7XDtxZFmvSyIX1qw266YyChlM"
AT = "1227127701191847936-V9cK4HPELzg5d4Xf1gwz134zk0onZC"
AS = "RNq5vWFRKM4An7jqlB5dfftcjbszUwQ1PwVYzdxKdJYkR"

auth = tweepy.OAuthHandler(CK, CS)
auth.set_access_token(AT, AS)

api = tweepy.API(auth)

try:
    sen_list = []
    for status in api.home_timeline(count=50):
        sentence = str(status.text).replace('\n', '')
        if len(sentence) <= 35:
            sen_list.append(sentence)
    tweet = tokenizer.generate_tweet(sen_list[random.randint(0, len(sen_list) - 1)])
    api.update_status(tweet)
except tweepy.error.RateLimitError as e:
    print(e)
    api.update_status("今、スマホで調べてるからちょっと待ってて")



