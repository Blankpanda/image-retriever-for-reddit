import praw
import sys


from entry import *


r = praw.Reddit(user_agent="Test Script by /u/blankpanda")

username  = get_username()
password  = get_password()
subreddit = get_subreddit_name()

get_limit = 1

r.login(username, password, disable_warning=True)

submissions = r.get_subreddit(subreddit).get_hot(limit = get_limit)
submissions = next(submissions)

print(submissions)
