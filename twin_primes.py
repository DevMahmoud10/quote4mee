import tweepy

# # def parse_primes(file):
# #     file = open(file, "r")
# #     data_file = file.read()
# #     data = []
# #     curStr = ''
# #     for c in data_file:
# #         if c.isdigit():
# #             curStr = curStr + c
# #         elif curStr != '':
# #             data.append(curStr)
# #             curStr = ''
# #         else:
# #             curStr = ''
    
# #     return ','.join(data)

# # data = parse_primes("twin_primes.txt")

consumer_token = 'g263nvk52IG47YxaeXCgUIL9H'
consumer_secret = '9FWw8U8aNwB0g9xklAIiPzSSbmeR5RZkqTiH0fOXyRHGYP7zAt'
ACCESS_TOKEN = '1050371798490120192-FPQAZiOLVrtyeLaVczxmPgr8ynOg67'
ACCESS_TOKEN_SECRET = 'rnPG31LhRVolMaLWRJGSIReQWfKnEPTArqIZGNkzioXA6'
# auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
# auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
# api = tweepy.API(auth)

# # last_tweet = api.user_timeline(screen_name = 'quote4mee',count=1)[0].text
# # last_posted_elem = last_tweet.split(',')[0]
# # next_index = data.index(last_posted_elem) + 1
# # twit = data[next_index] + ', ' + str(int(data[next_index]) + 2)
# twit = "Hello I`m Mahmoud"
# api.update_status(twit)

auth = tweepy.OAuthHandler(consumer_token, consumer_secret)
try:
    redirect_url = auth.get_authorization_url()
except tweepy.TweepError:
    print ('Error! Failed to get request token.')

auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

api = tweepy.API(auth)
api.update_status('tweepy + oauth!')