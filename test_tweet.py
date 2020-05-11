import tweepy
import random

import key

auth = tweepy.OAuthHandler(key.CK, key.CS)
auth.set_access_token(key.AT, key.AS)

api = tweepy.API(auth)

api.update_status("なんとなんと広町アップデートですー！毎日0時にフォロー返し忘れちゃった人を見つけてフォロバするようになりました〜。"
                  "あと、今開催中のイベントの台詞はイベント終了後に追加予定ですのでよろしくお願いしますー")