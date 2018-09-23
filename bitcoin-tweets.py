import praw
from datetime import datetime
import tweepy
from tweepy import OAuthHandler
import requests

now = datetime.now()
newsFile="/Users/cloudbool/Documents/RedditCryptoSub/CoinNews/"+str(now.month)+"-"+str(now.day)+"-"+str(now.year)+" News"
news=""

consumer_key = 'sdsdds'           # Replace with yours
consumer_secret = 'adfdfdfdfdf'   # Replace with yours
access_token = 'abcdefgh'         # Replace with yours
access_secret = 'abcdefgh'        # Replace with yours
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)

api = tweepy.API(auth)

class MyStreamListener(tweepy.StreamListener):

    def on_status(self, status):

        try:

            with open('newnewTweets.csv','a') as f:
                if status.user.followers_count>1000:
                    f.write(status.text.encode('utf-8')+" -")
                    f.write(str(status.user.followers_count))
                    f.write("\n")
        except Exception as e: # here catch whatever exception you may have.
            pass

myStreamListener = MyStreamListener()
myStream = tweepy.Stream(auth = api.auth, listener=myStreamListener)

myStream.filter(track=['bitcoin' ])
