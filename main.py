'''
#!/Library/Frameworks/Python.framework/Versions/3.6/bin/python3
'''

import tweepy
from time import sleep
import datetime

from config import create_api

def retweet(api, keywords):
    for tweet in tweepy.Cursor(api.search, q=('#leaders_in4thIR OR #leadership OR #LeadershipDevelopment -filter:retweer'), lang='en').items(1):
        try:
            print('\nTweet by: @' + tweet.user.screen_name)
            print('Time : ', datetime.datetime.now())
            tweet.retweet()
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
