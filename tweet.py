import tweepy
import random

import key
import tokenizer

auth = tweepy.OAuthHandler(key.CK, key.CS)
auth.set_access_token(key.AT, key.AS)

api = tweepy.API(auth)

try:
    sen_list = []
    for status in api.home_timeline(count=200):
        sentence = str(status.text).replace('\n', '')
        if len(sentence) <= 50 and len(sentence) >= 10:
            if "@" not in sentence and "質問" not in sentence and\
                    "おはよ" not in sentence and "普通" not in sentence and\
                    "笑" not in sentence and "おやすみ" not in sentence and\
                    "かわいい" not in sentence and "よろしく" not in sentence and\
                    "草" not in sentence and "w" not in sentence and "寝" not in sentence and\
                    "イベ" not in sentence and "協力" not in sentence and "なんで" not in sentence and\
                    "どうして" not in sentence:
                if "http" not in sentence:
                    if len(sentence) >= 30:
                        sentence = sentence[:30]
                    print(sentence)
                    sen_list.append(sentence)
    tweet = tokenizer.generate_tweet(sen_list[random.randint(0, len(sen_list) - 1)])
    api.update_status(tweet)
except:
    api.update_status("今、スマホで調べてるからちょっと待ってて")
    pass


