import json
import tweepy
from datetime import datetime
import pytz
import time
from collections import Counter

consumer_key = ""
consumer_secret = ""
access_token = ""
access_token_secret = ""

#Authorize to access Twitter REST API
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

#Instantiate Tweepy request
api = tweepy.API(auth)

#Extract hashtags from text
def extract_hashtags(tweet):
    '''Function get hashtags from entities within the tweet'''
    entities = tweet._json['entities']
    hashtags = entities['hashtags']
    return [ht['text'].lower() for ht in hashtags]
	
tweetData = []
hashtags = Counter()

# Public Twitter accounts related to Galway
search_public_pages = ["CTribune", "Galwaybayfmnews", "GalwayCityCo", "galwaytourism",
                      "galwayad", "GalwayGaillimh", "galway2020", "Galway2040", "GalwayCoCo"]
					  
# Twitter screen names of TDs associated with various political parties in Galway region
search_persons = ["MichealMartinTD", "AnneRabbitte", "ciarancannon", 
                  "1Hildegarde", "catherinegalway", "SeanKyneTD"]
				  
# Combine search terms from both public pages as well as individual users
searchTerms = search_public_pages + search_persons

#Iterate through all search terms and find releveant tweets
for term in searchTerms:
    try:
	#Query REST API as per limits (after every 5 seconds) to avoid failed requests
        print(f'Retrieving tweets from @{term}...')
        time.sleep(5)
        tweetsFromUser = api.user_timeline(screen_name = term,
                                  count = 1000, 
                                  include_rts = True)
								  

        for tweet in tweetsFromUser:
            tweetDate = datetime.strptime(tweet._json['created_at'], '%a %b %d %H:%M:%S %z %Y')
			#Get all tweets from 1st Sep, 2017 (past 6 months)
            if tweetDate > pytz.utc.localize(datetime(2017, 9, 1)):
                status = {}
                status['id'] = tweet._json['id']
                status['retweet_count'] = tweet._json['retweet_count']
                status['favorite_count'] = tweet._json['favorite_count']
                status['text'] = tweet._json['text']

                if tweet._json['in_reply_to_status_id']:
                    status["in_reply_to_status_id"] = tweet._json['in_reply_to_status_id']
                else:
                    status["in_reply_to_status_id"] = -1
                tweet_hashtags = extract_hashtags(tweet)
                hashtags.update(tweet_hashtags)


                tweetData.append(status)
    except:
        print(f'Failed for term {term}')


#Dump Tweets to JSON file
with open('Tweets.json', 'w') as outfile:
    json.dump(tweetData, outfile)
print(f'\n{len(tweetData)} tweets downloaded and saved to file, Tweets.json')
