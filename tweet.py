import tweepy
import random

import key
import tokenizer

auth = tweepy.OAuthHandler(key.CK, key.CS)
auth.set_access_token(key.AT, key.AS)

api = tweepy.API(auth)
Twitter_ID = str(api.me().screen_name)

ng_word = ["@", "質問", "おは", "普通", "おやすみ", "かわいい", "よろ", "w", "WW",
           "寝", "イベお", "乙", "協力", "なんで", "ふざけん", "！！",
           "どうして", "なぜ", "何故", "ありがと", "(", ")", ".", "・・", "…", "RT", "ＲＴ", "どこ", "誰", "だれ",
           "かっこ", "イベ乙", "ああ", "ぁぁ", "ぉぉ", "おお", "ぇぇ", "ええ", "まじで", "マジで", "かよ", "shindan",
           "殺", "ほか", "定期"]

try:
    sen_list = []
    for status in api.home_timeline(count=300):
        check = False
        if status.user.screen_name == Twitter_ID:
            continue
        sentence = str(status.text).replace('\n', '')
        if 50 >= len(sentence) >= 10:
            for word in ng_word:
                if word in sentence:
                    check = True
            if not check:
                if "http" not in sentence and sentence[0] != "#" and ("死" not in sentence or "爆死" in sentence)\
                        and sentence[-1] != "ー" and ("笑" not in sentence or "笑う" in sentence
                                                     or "笑え" in sentence or "笑っ" in sentence):
                    if len(sentence) >= 30:
                        sentence = sentence[:30]
                    print(sentence, tokenizer.generate_tweet(sentence))
                    sen_list.append(sentence)
    tweet = tokenizer.generate_tweet(sen_list[random.randint(0, len(sen_list) - 1)])
    api.update_status(tweet)
except:
    api.update_status("今、スマホで調べてるからちょっと待ってて")
    pass


