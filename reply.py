# -*- coding: utf-8 -*-
import tweepy
import key
import random
#from requests_oauthlib import OAuth1Session

Twitter_ID = "hiromachinanami"
SCREEN_NAME = '普通bot'

auth = tweepy.OAuthHandler(key.CK, key.CS)
auth.set_access_token(key.AT, key.AS)

api = tweepy.API(auth)
timeline = api.mentions_timeline(count=1)

f = open("/Users/iwasaka/PycharmProjects/Nanamin/texts/response.txt", "r")
l = f.readlines()
response = "".join(random.sample(l,1))

for status in timeline:
      status_id = status.id
      screen_name = status.author.screen_name
      scrn = screen_name.replace(' ', '')
      scr = scrn.rstrip('\n')
      print("@" + scr)
      print(status.text)
      inp = status.text
      inp = inp.lstrip("@hiromachinanami")
      print(inp)
      res = response
      try:
          res = response.replace("Name", status.user.name)
      except:
          pass
      reply_text="@" + screen_name + " " + res
      api.create_favorite(status.id)
      if str(status.in_reply_to_screen_name) == Twitter_ID and str(status.user.screen_name) != Twitter_ID:
          api.update_status(status=reply_text, in_reply_to_status_id=status_id)
      else:
          print("エラー")