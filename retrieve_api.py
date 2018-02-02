import simplejson as json
from common.credentials import ACCESS_TOKEN, ACCESS_SECRET, CONSUMER_KEY, CONSUMER_SECRET
from twitter import Twitter, OAuth, TwitterHTTPError, TwitterStream

oauth = OAuth(ACCESS_TOKEN, ACCESS_SECRET, CONSUMER_KEY, CONSUMER_SECRET)

twitter_stream = TwitterStream(auth=oauth)
iterator = twitter_stream.statuses.sample()


for tweet in iterator:
    print (json.dumps(tweet))