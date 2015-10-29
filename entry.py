import sys
import getpass

def get_username():

    while True:

        username = input("Enter username: ")

        if username != "":
            return "" + username
        else:
            continue

def get_password():

    while True:

        password = getpass.getpass("Enter password: ")

        if password != "":
            return password
        else:
            continue

def get_subreddit_name():

    while True:

    subreddit = input("Enter subreddit name: ")

    if subreddit != "":
        return subreddit
    else:
        continue
