#ランダムツイートプログラム
import tweepy
import random
import os

#---------定型文----------
CONSUMER_KEY = "取得したAPI key"
CONSUMER_SECRET = "取得したAPI secret key"
ACCESS_TOKEN = "取得したAccess token"
ACCESS_SECERET = "取得したAccess token secret"

#OAuth認証
auth = tweepy.OAuthHandler(CONSUMER_KEY,CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN,ACCESS_SECERET)

#TwitterAPIオブジェクト
api = tweepy.API(auth, wait_on_rate_limit = True)
#-----------------------

#ツイートする文章
tweetList = ['テスト投稿','はじめまして\nこんにちわ','バーチャルYoutuberのアカリです']

#前回ツイートした内容のIndexを取得する
before_num = 0
path = os.path.dirname(__file__) + "/save.dat"
if os.path.isfile(path):
	with open(path) as f:
		before_num = f.readlines()

#前回と違うツイートを選ぶ
choice_num = 0
while 1:
	num = random.randint(0, len(tweetList) - 1)
	if num != before_num:
		choice_num = num
		with open(path,mode='w') as f:
			f.write(str(choice_num))
		break

#ツイートする
#print(choice_num, tweetList[choice_num])
api.update_status(tweetList[choice_num])