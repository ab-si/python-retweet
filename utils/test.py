'''
Functions to test for some small twitter APIs
'''

# Test Tweet
def test_tweet(api):
    api.update_status("Test tweet from Tweepy Python")

