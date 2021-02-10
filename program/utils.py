import tweepy

CONSUMER_KEY = "取得したAPI key"
CONSUMER_SECRET = "取得したAPI secret key"
ACCESS_TOKEN = "取得したAccess token"
ACCESS_SECERET = "取得したAccess token secret"
#自分のTwitter IDを入れる
SCREEN_NAME = ""
#ツイートを検索する際、リツイートやリプライのツイートは除外する
SEARCH_FILTER = " -filter:retweets -filter:replies"

def GetTwitterAPI():
	#OAuth認証
	auth = tweepy.OAuthHandler(CONSUMER_KEY,CONSUMER_SECRET)
	auth.set_access_token(ACCESS_TOKEN,ACCESS_SECERET)

	#TwitterAPIオブジェクト
	#API利用制限にかかった場合、解除まで待機する
	return tweepy.API(auth, 
		wait_on_rate_limit = True,#API利用制限にかかった場合、解除まで待機する
		wait_on_rate_limit_notify = True)#API利用制限解除されるのを待っている時に通知を表示する