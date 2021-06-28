import json
from pytwitter import Api
import os


class TwitterAPI_V2:
    """A library that provides a Python interface to the Twitter API"""
    BEARER_TOKEN = "AAAAAAAAAAAAAAAAAAAAAG64QwEAAAAAO3B90btcZOQltdBSLlIs4IP%2BIec%3DK7HsCRd8JLpKS81ZVKOfudMmL2vXa9f6yN2Rgf4IjMBHNLxmJD"

    def __init__(self):
        self.api = Api(bearer_token=TwitterAPI_V2.BEARER_TOKEN)


    def getTweets(self, start_time, nextToken=None):
        if nextToken == "":
            nextToken = None
        response = self.api.search_tweets(
            query='"."',
            query_type="recent",
            start_time=start_time,
            max_results=100,
            return_json=True,
            expansions="author_id", 
            tweet_fields=["created_at", "entities"], 
            user_fields=["username","verified"],
            next_token = nextToken
        )
        response_formatted = json.dumps(response)
        tweets = json.loads(response_formatted)
        return tweets