import tweepy
import random

import key

auth = tweepy.OAuthHandler(key.CK, key.CS)
auth.set_access_token(key.AT, key.AS)

api = tweepy.API(auth)

api.update_status("なんとなんと、広町アップデートしましたー！毎日0時にフォローを返し忘れちゃった人を見つけてフォロバしに行きます〜！"
                  "あと、現在開催しているイベントでの台詞はイベント終了後に追加する予定ですのでネタバレはしませんよー")