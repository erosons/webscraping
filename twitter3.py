from tweepy import API
from tweepy import Cursor
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
import twittercredentialshidden  # This is my hidden file credential imported

### Twiiter Client ####
# This twitter_user gives the privilege for a different user and whete None it use my profile


class TwitterClient():
    def __init__(self, twitter_user=None):
        self.auth = TwitterAuthenticator().authenticate_twitter_app()
        self.twitter_client = API(self.auth)

        self.twitter_user = twitter_user

    def get_user_timeline_tweets(self, num_tweets):
        tweets = []
        for tweet in Cursor(self.twitter_client.user_timeline, id=self.twitter_user).items(num_tweets):
            tweets.append(tweet)
        return tweets

    def get_home_timeline_tweets(self, num_home):
        home_tweets = []
        for home in Cursor(self.twitter_client.home_timeline).items(num_home):
            home_tweets.append(home)
        return home_tweets

### TWITTER AUTHENTICATER####


class TwitterAuthenticator():

    def authenticate_twitter_app(self):
        auth = OAuthHandler(twittercredentialshidden.consumer_key,
                            twittercredentialshidden.consumer_secret)
        auth.set_access_token(twittercredentialshidden.token_key,
                              twittercredentialshidden.token_secret)
        return auth


class Twitter_Streamer():
    """
    Class for streaming and processing live tweets
    """

    def __init__(self):
        self.twitter_authenticator = TwitterAuthenticator()

    def stream_tweets(self, fetch_tweets_filname, hash_tag_list):
        # This handles Twitter authentication and the connection the Twitter streaming API
        listner = TwitterListner(fetch_tweets_filname)
        auth = self.twitter_authenticator.authenticate_twitter_app()
        stream = Stream(auth, listner)
        # This line filter Steams to capture data by the keywords
        stream.filter(track=hash_tag_list)


class TwitterListner(StreamListener):
    """
    This a basic listner class that jusr prints recieved tweets to stdout.
    """

    def __init__(self, fetch_tweets_filname):
        self.fetch_tweets_filname = fetch_tweets_filname

    def on_data(self, data):
        try:
            print(data)
            with open(self.fetch_tweets_filname, "a") as tf:
                tf.write(data)
            return True
        except BaseException as e:
            print("Error on data: %s" % str(e))
        return True

    def on_error(self, status):
        if status == 420:
            # Return False on_data method in case rate limit is abused or occurs
            return False
        print(status)
        return True


if __name__ == "__main__":
    hash_tag_list = ["covid-19", "Joe Biden",
                     "Outbound sales", "Commercial Broker", "Gas Prices"]
    fetch_tweets_filname = "tweets.json"
    fetch_tweets_filname = "home_tweets.json"
    twitter_clients = TwitterClient("gas_prices_news")
    print(twitter_clients.get_user_timeline_tweets(10))

  #  twiter_streamer = Twitter_Streamer()
  #  twiter_streamer.stream_tweets(fetch_tweets_filname, hash_tag_list)
