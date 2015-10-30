import praw
import sys
import urllib

from entry import *


r = praw.Reddit(user_agent="Test Script by /u/blankpanda")

username = get_username()
password = get_password()
subreddit_name = get_subreddit_name()

request_limit = 10

r.login(username, password, disable_warning=True)

submissions = r.get_subreddit(subreddit_name).get_top(limit = request_limit)

count = 0

for submission in submissions:
    urllib.request.urlretrieve(submission.url, "test" + str(count) + ".jpg")
    count += 1
