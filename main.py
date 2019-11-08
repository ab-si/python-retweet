import tweepy
from time import sleep

from config import create_api

def retweet(api, keywords):
    for tweet in tweepy.Cursor(api.search, q=('#ayodhyaverdict'), lang='en').items(1):
        try:
            print('\nTweet by: @' + tweet.user.screen_name)
            tweet.retweet()
            print('Tweet Retwitted')
        except tweepy.TweepError as e:
            print(e.reason)
        except StopIteration:
            break

def favourite(api, keywords):
    for tweet in tweepy.Cursor(api.search, q=('#liverpool'),lang='en').items(1):
        try:
            print('\nTweet by: @' + tweet.user.screen_name)
            tweet.favorite()
            print('Like the tweet')
            sleep(5)
        except tweepy.TweepError as e:
            print(e.reason)
        except StopIteration:
            break

def main():
    api = create_api()
    retweet(api, "noone")


if __name__ == "__main__":
    main()
