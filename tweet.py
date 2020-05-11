import tweepy
import random

import key
import tokenizer

auth = tweepy.OAuthHandler(key.CK, key.CS)
auth.set_access_token(key.AT, key.AS)

api = tweepy.API(auth)

try:
    sen_list = []
    for status in api.home_timeline(count=300):
        if status.user.screen_name == "hiromachinanami":
            continue
        sentence = str(status.text).replace('\n', '')
        if len(sentence) <= 50 and len(sentence) >= 10:
            if "@" not in sentence and "質問" not in sentence and\
                    "おはよ" not in sentence and "普通" not in sentence and\
                    "笑" not in sentence and "おやすみ" not in sentence and\
                    "かわいい" not in sentence and "よろしく" not in sentence and\
                    "草" not in sentence and "w" not in sentence and "寝" not in sentence and\
                    "イベお" not in sentence and "協力" not in sentence and "なんで" not in sentence and\
                    "どうして" not in sentence and "ありがと" not in sentence and "(" not in sentence and\
                    ")" not in sentence and "..." not in sentence and "…" not in sentence and\
                    "?" not in sentence and sentence[-1:] != "!" and "？" not in sentence and\
                    sentence[-1:] != "！" and "RT" not in sentence and "RT" not in sentence and\
                    "どこ" not in sentence and "誰" not in sentence and "だれ" not in sentence and\
                    "かっこよ" not in sentence and "イベ乙" not in sentence and "・・・" not in sentence and\
                    sentence[0] != "#" and "あああ" not in sentence and "ぁぁぁ" not in sentence and\
                    "まじで" not in sentence and "マジで" not in sentence:
                if "http" not in sentence:
                    if len(sentence) >= 30:
                        sentence = sentence[:30]
                    print(sentence,tokenizer.generate_tweet(sentence))
                    sen_list.append(sentence)
    tweet = tokenizer.generate_tweet(sen_list[random.randint(0, len(sen_list) - 1)])
    api.update_status(tweet)
except:
    api.update_status("今、スマホで調べてるからちょっと待ってて")
    pass


