import tweepy
import random

import key
import tokenizer

auth = tweepy.OAuthHandler(key.CK, key.CS)
auth.set_access_token(key.AT, key.AS)

api = tweepy.API(auth)

try:
    sen_list = []
    for status in api.home_timeline(count=100):
        sentence = str(status.text).replace('\n', '')
        if len(sentence) <= 50 and len(sentence) >= 10:
            if "@" not in sentence:
                if "http" not in sentence or "t.co" in sentence:
                    if len(sentence) >= 30:
                        sentence = sentence[:30]
                    print(sentence)
                    sen_list.append(sentence)
    tweet = tokenizer.generate_tweet(sen_list[random.randint(0, len(sen_list) - 1)])
    api.update_status(tweet)
except:
    api.update_status("今、スマホで調べてるからちょっと待ってて")
    pass


