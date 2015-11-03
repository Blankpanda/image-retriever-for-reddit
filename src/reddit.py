import praw, sys, urllib, re, os
from entry import *
from downloader import *

request_limit = 25


r = praw.Reddit(user_agent="Awwnime Image Grabber for Reddit /u/blankpanda")

#username = get_username()
#password = get_password()
subreddit_name = get_subreddit_name()


#r.login(username, password, disable_warning=True)

submissions = r.get_subreddit(subreddit_name).get_hot(limit = request_limit)

# downloads images
for submission in submissions:
    tag = re.search("\[(.*?)\]", submission.title)
    folder_name = tag.group(0)

    if os.path.exists(folder_name):
        append_image_to_existing_directory(
        submission.url,
        folder_name,
        submission.id
        )
    else:
        download_image(
        submission.url,
        folder_name,
        submission.id
        )
