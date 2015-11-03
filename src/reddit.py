import praw, sys, urllib, re, os
from entry import *
from downloader import *

request_limit = 25


r = praw.Reddit(user_agent=" Image Grabber for Reddit by /u/blankpanda")

subreddit_name = get_subreddit_name()

submissions = r.get_subreddit(subreddit_name).get_hot(limit = request_limit)

# downloads images
for submission in submissions:
    tag = re.search("\[(.*?)\]", submission.title)

    if tag == None:
        if os.path.exists("tagless"):
            download_image_tagless_append(
            submission.url,
            submission.id
            )
        else:
            download_image_tagless(
            submission.url,
            submission.id
            )

    else:
        folder_name = tag.group(0)

        if os.path.exists(folder_name):
            download_image_append(
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
