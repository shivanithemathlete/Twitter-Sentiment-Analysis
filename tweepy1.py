import tweepy
from textblob import TextBlob
import csv

consumer_key='2UxNXthi4C5zAgg66Jj3hbZSP'
consumer_secret='gR4DoPpvLdeDWDRlf1vSrMZvqMFwKD8Hjq7NpFnA0eAwdrdWFq'


access_token='1226516164622213120-gCVW4vPPKv3dpAa2Sx1gnkIa8ReuZW'
access_token_secret='hVb8afGIcw1qUfH7LOcVBzjl3QDAfVm8OY1T9pM6DqPWR'

auth=tweepy.OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_token,access_token_secret)

api=tweepy.API(auth)
#file_handling

with open('twwepy1.csv','w',newline='') as f:
    thewriter=csv.writer(f)
    thewriter.writerow(['Tweet','Sentiment_Analysis'])

#search n collect tweets with certain keywords
threshold=0
public_tweets=api.search('Trump')
for tweet in public_tweets:
    analysis=TextBlob(tweet.text)
    if analysis.sentiment.polarity>threshold:
        sentiment='Positive'
    else:
        sentiment='Negative'
    with open('twwepy1.csv','a',newline='') as f:
        thewriter=csv.writer(f)
        thewriter.writerow([tweet.text,sentiment])
    
##    print(analysis.sentiment)
    
