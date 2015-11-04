import praw, sys, urllib, re, os
from entry import *
from downloader import *
from imgur import *

request_limit = 10


r = praw.Reddit(user_agent=" Image Grabber for Reddit by /u/blankpanda")

subreddit_name = get_subreddit_name()

submissions = r.get_subreddit(subreddit_name).get_top_from_all(limit = request_limit)


# downloads single images create a list of the albums
for submission in submissions:

    if "/a/" in submission.url:
        print(submission.url)
        download_imgur_album(submission.url)


    tag = re.search("\[(.*?)\]", submission.title) # retrieves tag in brackets.

    if tag == None: # the regex didnt find anything
        if os.path.exists("tagless"): # the tagless folder already exists
            download_image_tagless_append(
            submission.url,
            submission.id
            )
        else: # the tagless folder needs to be created
            download_image_tagless(
            submission.url,
            submission.id
            )

    else: # the regex returned something
        folder_name = tag.group(0)

        if os.path.exists(folder_name): # the folder already exists
            download_image_append(
            submission.url,
            folder_name,
            submission.id
            )
        else: # the folder needs to be created
            download_image(
            submission.url,
            folder_name,
            submission.id
            )

#download imgur albums
