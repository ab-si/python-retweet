#!/Library/Frameworks/Python.framework/Versions/3.6/bin/python3

import tweepy
from time import sleep
import datetime

from config import create_api

def retweet(api, keywords):
    count = 0
    max_try = 0
    while count <= 0 or max_try < 5:
        tweet = tweepy.Cursor(api.search, q=('#leaders_in4thIR OR #leadership OR #LeadershipDevelopment -filter:retweer'), lang='en').items(10)
        for t in tweet:
            try:
                if t.retweet_count >= 10:
                    print('\nTweet by: @' + t.user.screen_name)
                    print('Time : ', datetime.datetime.now())
                    t.retweet()
                    count += 1
            except t.TweepError as e:
                print(e.reason)
            except StopIteration:
                break
        max_try += 1


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
