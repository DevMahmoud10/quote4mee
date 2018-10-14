import tweepy

import time
import atexit

from apscheduler.schedulers.background import BackgroundScheduler

consumer_token = 'g263nvk52IG47YxaeXCgUIL9H'
consumer_secret = '9FWw8U8aNwB0g9xklAIiPzSSbmeR5RZkqTiH0fOXyRHGYP7zAt'
ACCESS_TOKEN = '1050371798490120192-FPQAZiOLVrtyeLaVczxmPgr8ynOg67'
ACCESS_TOKEN_SECRET = 'rnPG31LhRVolMaLWRJGSIReQWfKnEPTArqIZGNkzioXA6'

def tweetNow():
    text="Ayaad"
    auth = tweepy.OAuthHandler(consumer_token, consumer_secret)
    try:
        redirect_url = auth.get_authorization_url()
    except tweepy.TweepError:
        print ('Error! Failed to get request token.')

    auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

    api = tweepy.API(auth)
    api.update_status(text)

scheduler = BackgroundScheduler()
scheduler.add_job(func=tweetNow, trigger="interval", seconds=120)
scheduler.start()

# Shut down the scheduler when exiting the app
atexit.register(lambda: scheduler.shutdown())



