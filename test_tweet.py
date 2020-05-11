import tweepy
import random
import json
import urllib.request

import key

url = 'http://ns.dena.jp/mbga/gameapi//v1/ngword?_method=check&format=json'
data = {
    'data': "「殺す」はNGワードであるか",
}
headers = {
    'Content-Type': 'application/json',
}

req = urllib.request.Request(url, json.dumps(data).encode(), headers)
with urllib.request.urlopen(req) as res:
    body = res.read()
    print(body)

# auth = tweepy.OAuthHandler(key.CK, key.CS)
# auth.set_access_token(key.AT, key.AS)
#
# api = tweepy.API(auth)

# api.update_status("今から運動してきますだいたい5キロか6キロくらい走るのって普通……だよね？")