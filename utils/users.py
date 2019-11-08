'''
This file contains some some utility to check for API validations,
error messages, and different utilities
'''

# Testing the credentials
def check_login(api):
    try:
        api.verify_credentials()
        return True
    except:
        return False

# Get Username
def get_user(api):
    return api.me()

# Get user timelines
# It will get last 20 tweets in the user timeline
def get_user_timeline(api):
    timeline = api.home_timeline()
    for tweet in timeline:
        print(f"{tweet.user.name} said {tweet.text}")

# Search users
def search_user(api, user):
    return api.get_user(user)
    
# Print some user info
def print_user(user):
    print(user.name)
    print(user.description)
    print(user.location)

    for follower in user.followers():
        print(follower.name)