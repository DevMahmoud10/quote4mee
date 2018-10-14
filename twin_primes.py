import tweepy

def parse_primes(file):
    file = open(file, "r")
    data_file = file.read()
    data = []
    curStr = ''
    for c in data_file:
        if c.isdigit():
            curStr = curStr + c
        elif curStr != '':
            data.append(curStr)
            curStr = ''
        else:
            curStr = ''
    
    return ','.join(data)

data = parse_primes("twin_primes.txt")

CONSUMER_KEY = 'xW5vBk2vBPZLBG4cL4fkaehk2'
CONSUMER_SECRET = 'QlCKicmXXwTpSGOXOChnN1vARBvOQUEwpmL9NSBzuEWfDRC5AT '
ACCESS_TOKEN = '1050371798490120192-cpDgjuUuR8CCRkYO6O1TePcGKtsMls'
ACCESS_TOKEN_SECRET = 'zH8zoYuogIkCC4BxAdV7DQ5ej0JkO9PKJZrrWjn6iwywU'
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)

last_tweet = api.user_timeline(screen_name = '_twin_primes',count=1)[0].text
last_posted_elem = last_tweet.split(',')[0]
next_index = data.index(last_posted_elem) + 1
twit = data[next_index] + ', ' + str(int(data[next_index]) + 2)
api.update_status(twit)