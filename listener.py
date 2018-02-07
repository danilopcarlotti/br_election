from common.credentials import ACCESS_TOKEN, ACCESS_SECRET, CONSUMER_KEY, CONSUMER_SECRET
from tweepy import *

class StreamListener(tweepy.StreamListener):
	"""Class with methods for the retrieval of data"""
	def __init__(self, arg):
		self.arg = arg
		self.auth = OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
		self.auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)
		self.api = tweepy.API(self.auth)

	def on_status(self, status):
	    date_twitt = status.created_at
	    id_t = status.id
	    in_reply_status = status.in_reply_to_status_id
	    in_reply_user = status.in_reply_to_user_id
	    user = status.user
	    reply_count = status.reply_count
	    retweet_count = status.retweet_count
	    favorite_count = status.favorite_count
	    entities = status.entities
		extended_entities = status.extended_entities
	    texto = status.text

	def on_error(self, status_code):
	    if status_code == 420:
	        return False
