#-*- coding:utf-8 -*-
import tweepy
import key
from recognization import ocr

auth = tweepy.OAuthHandler(key.CK, key.CS)
auth.set_access_token(key.AT, key.AS)
api = tweepy.API(auth)

Twitter_ID = str(api.me().screen_name)
filter_ID = "@" + Twitter_ID


class MyStreamListener(tweepy.StreamListener):
    def on_status(self, status):
        status_id = status.id
        screen_name = status.user.screen_name
        if status.text != "画像認識テスト":
            entities = status.entities
            if "media" in entities:
                media = entities["media"]
                reply_text = "ちょっと画像が読み込めなかったみたい…ごめんね、Name先輩…"
                try:
                    reply_text = ocr.screen_ocr(media[0]['media_url'])
                except:
                    pass
                if "Name" in reply_text:
                    reply_text = reply_text.replace("Name", str(status.user.name))
                api.update_status(status=reply_text, in_reply_to_status_id=status_id)

stream = tweepy.Stream(auth, MyStreamListener())
while True:
    try:
        stream.filter(track=["hiromachitest"])
    except KeyboardInterrupt:
        stream.disconnect()
        break
    except Exception as e:
        stream.disconnect()
        print(e)