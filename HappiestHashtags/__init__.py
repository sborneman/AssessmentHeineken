import logging
from datetime import datetime, timedelta
import time
from collections import Counter
from twitter import TwitterAPI_V2
import azure.functions as func
import logging
import azure.functions as func


# Azure Function Timer Trigger (Happiest Hashtags)
def main(mytimer: func.TimerRequest) -> None:
    last_hour_date_time = datetime.utcnow() - timedelta(minutes=60)
    last_hour = last_hour_date_time.isoformat("T") + "Z"
    next_token = ""
    happy_tweets_hashtags = []
    api = TwitterAPI_V2()

    while next_token is not None:
        try:
            tweets = api.getTweets(last_hour, next_token)
            for tweet in tweets['data']:
                if ":)" in tweet['text']:
                    author_id = tweet['author_id']
                    tweet_id = tweet['id']
                    print(f"https://twitter.com/{author_id}/status/{tweet_id}")
                    logging.info(f"log: https://twitter.com/{author_id}/status/{tweet_id}")
                    if "entities" in tweet:
                        if "hashtags" in tweet['entities']:
                            for hashtag in tweet['entities']['hashtags']:
                                happy_tweets_hashtags.append(hashtag['tag'])
                next_token = tweets.get('meta').get('next_token')
        except:
            print("Rate limit exceeded.")
            print("Waiting for 5 minutes...")
            time.sleep(300)
            print("Rerun started...")

    print("Happiest hashtags in the past hour:")
    c = Counter(happy_tweets_hashtags)
    print(c.most_common(5))
