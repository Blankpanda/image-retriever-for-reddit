import sys
import getpass

def get_username():
    # gets the reddit username of the user
    while True:
        username = input("Enter username: ")
        if username != "":
            return "" + username
        else:
            continue

def get_password():
    # gets the reddit password associated with the username
    while True:
        password = getpass.getpass("Enter password: ")
        if password != "":
            return password
        else:
            continue

def get_subreddit_name():
    # gets the name of the subreddit thats being queried
    while True:
        subreddit = input("Enter subreddit name: ")
        if subreddit != "":
            return subreddit
        else:
            continue
