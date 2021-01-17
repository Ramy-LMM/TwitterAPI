#ツイートテストのプログラム

#---------定型文----------
import tweepy

CONSUMER_KEY = "取得したAPI key"
CONSUMER_SECRET = "取得したAPI secret key"
ACCESS_TOKEN = "取得したAccess token"
ACCESS_SECERET = "取得したAccess token secret"

#OAuth認証
auth = tweepy.OAuthHandler(CONSUMER_KEY,CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN,ACCESS_SECERET)

#TwitterAPIオブジェクト
api = tweepy.API(auth)
#-----------------------

#ツイートをする
api.update_status("API テスト投稿")