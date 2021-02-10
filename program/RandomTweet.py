#ランダムツイートプログラム
import tweepy
import random
import os

#---------定型文----------
CONSUMER_KEY = "1lYzTJS40nztdeG9n6Ppphc1C"
CONSUMER_SECRET = "l7NJeCRTEENL1ZlO5mpvhIWsyl4I1URAg3102SsoN2se4Mmy4K"
ACCESS_TOKEN = "830478227525169152-6lb9JVIc8W7fpp9Lj2L7nxGSrneiMLW"
ACCESS_SECERET = "2EyRbAAJu5qRdidE95fSxxdNe0DrjfPJszB5sg8MGf5LO"

#OAuth認証
auth = tweepy.OAuthHandler(CONSUMER_KEY,CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN,ACCESS_SECERET)

#TwitterAPIオブジェクト
api = tweepy.API(auth, wait_on_rate_limit = True)
#-----------------------

#ツイートする文章
#tweetList = ['テスト投稿','はじめまして\nこんにちわ','バーチャルYoutuberのアカリです']
tweetList = [
'''
【定期ツイート】
皆様はじめまして
マインクラフトに解説系、マンガレビュー
様々な動画を上げているリトルメイドVTuberです
お気に入りの動画がきっと見つかります！

↓チャンネル登録宜しくお願いします！↓
http://bit.ly/2Yzpw6d

#VTuber #Minecraft #LittleMaidMob
https://twitter.com/Revenging_maid/status/1351010941916360706/photo/1
''',
'''
【定期ツイート】
マインクラフトに漫画レビュー、解説系
様々な動画を上げているリトルメイドVTuberです
お気に入りの動画がきっと見つかります！
↓チャンネル登録宜しくお願いします↓
http://bit.ly/2Yzpw6d

#Vtuber好きさんと繋がりたい
#Vtuber好きと繋がりたい
https://twitter.com/Revenging_maid/status/1351010941916360706/photo/1
''',
'''
【定期ツイート】
マインクラフトに漫画レビュー、解説系
様々な動画を上げているリトルメイドVTuberです
お気に入りの動画がきっと見つかります！
↓チャンネル登録宜しくお願いします↓
http://bit.ly/2Yzpw6d

#YouTuber好きな人と繋がりたい
#Vtuber好きと繋がりたい
https://twitter.com/Revenging_maid/status/1351010941916360706/photo/1
''',
'''
【定期ツイート】
マインクラフトにマンガレビュー、解説系
様々な動画を上げてるリトルメイドVTuberです
お気に入りの動画がきっと見つかります
↓チャンネル登録宜しくお願いします↓
http://bit.ly/2Yzpw6d

#YouTuber好きな人と繋がりたい
#Vtuber好きさんと繋がりたい
https://twitter.com/Revenging_maid/status/1351010941916360706/photo/1
''',
]

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