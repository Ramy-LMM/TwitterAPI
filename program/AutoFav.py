#フォロワーじゃない人で、関心のあるツイートをしているツイートにいいねをしまくるプログラム
#いいねは1日に1000件がMAX
#また、高速でいいねをしていくと、スパム扱いをされ制限や凍結を受けるので注意
import tweepy
import datetime
import time
import utils

api = utils.GetTwitterAPI()

#24時間分のデータを取得するための変数
now = datetime.datetime.now()
yesterday = now - datetime.timedelta(days = 1)
#スパム扱いされているかどうか
is283 = False
#検索リスト
q_list = [
'LittleMaidMob', 
'リトルメイド', 
'#マインクラフト', 
'#Minecraft', 
'マイクラ', 
'#Vtuber好きと繋がりたい', 
'#vtuber好きな人と繋がりたい', 
'#Vtuberさんと繋がりたい',
'#おはようVtuber',
]

print("開始時刻：" + now.strftime('%Y-%m-%d_%H:%M:%S'))
for word in q_list:
	print("「" + word + "」の検索を開始")
	tweets = tweepy.Cursor(api.search, q = word + utils.SEARCH_FILTER,\
		#エンティティを入れる
		include_entities = True,\
		#Tweet全文を取得する
		tweet_mode = 'extended',\
		#最新のツイートを取得する その他→mixed：人気のと最新のと織り交ぜる popular：人気のツイートのみ取得
		result_type = 'recent',\
		since = yesterday.strftime('%Y-%m-%d_%H:%M:%S_JST'),\
		until = now.strftime('%Y-%m-%d_%H:%M:%S_JST'),
		#日本語のツイートのみ取得
		lang = 'ja').items(200) #100ツイートを取得する。何も指定しなければ、限界まで取得してくる

	#自分のフォロワーのIDを取得する
	followers = api.followers_ids(utils.SCREEN_NAME)
	count = 0
	for tweet in tweets:
		#「フォロワーじゃない人」と「自分以外」を選ぶ
		if (tweet.user.screen_name in followers) or (tweet.user.screen_name == utils.SCREEN_NAME):
			continue
		#既にいいね！をしていないツイートを選ぶ
		tweet_status = api.get_status(tweet.id)
		if tweet_status.favorited:
			continue
		#if tweet.favorited:
		#	continue
		"""
		print('＝＝＝＝＝＝＝＝＝＝')
		print('twid : ',tweet.id)
		print('user : ',tweet.user.screen_name)
		print('date : ', tweet.created_at)
		print(tweet.full_text)
		print('favo : ', tweet.favorite_count)
		print('favorited : ', tweet.favorited)
		print('retw : ', tweet.retweet_count)
		"""

		#いいね！をする
		try:
			api.create_favorite(tweet.id)
		except Exception as e:
			print(e.reason)
			if "429" in e.reason:
				print("回数制限を超えたので、待機します。")
				time.sleep(60 * 15)
			if "283" in e.reason:
				print("スパムと誤解されているので、プログラムを中止します。")
				is283 = True;
				break
		#高速でやり続けるのが怖いので、一応待機
		time.sleep(5)
		count+=1
		if count >= 30:
			break
	if is283:
		break