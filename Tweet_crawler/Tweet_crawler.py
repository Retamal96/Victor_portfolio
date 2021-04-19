import tweepy

#keys provided by twitter
costumer_key = input("insert costumer key")
costumer_secrete = input("insert costumer secrete")
access_token = input("insert access_token")
access_secret = input("insert access_secret")

#parameters
tweetsQuery = 1
MaxTweets = 10
hashtags = '#hashtasg'
maxId = -1
tweetcount = 0

#connection to twitter
authentication = tweepy.OAuthHandler(consume_key, consumer_secret)
authentication.set_access_token(access_token, access_secret)
api = tweepy.API(authentication, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

#collect data
while tweetcount < MaxTweets:
    if (maxId <= 0 ):
        newTweets = api.search(q=hashtags,count=tweetsQuery, result_type='recent', tweet_mode='extended')
    else:
        newTweets = api.search(q=hashtags, count = tweetsQuery, max_id = str(maxId - 1), result_type='recent', tweet_mode='extended')
    
    #NewTweets not found
    if not newTweets:
        print('No tweets')
        break
    for tweet in newTweets:
        print(tweet.full_text.encode('utf-8'))

    #update parameters 
    tweetCount += len(newTweets)
    maxId = newTweets[-1].id