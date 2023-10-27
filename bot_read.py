#!/usr/bin/python
import praw
import pdb
import re
import os

reddit = praw.Reddit('bot1')

learnpython = reddit.subreddit("learnpython")
python = reddit.subreddit("python")
learnprogramming = reddit.subreddit("learnprogramming")

def getSubmissions(subreddit, flair=False):
    for submission in subreddit.hot(limit=5):
        print("Title: ", submission.title)
        print("Text: ", submission.selftext)
        print("Score: ", submission.score)
        if flair:
            print("Flair: ", submission.link_flair_text.strip().lower())
        print("---------------------------------\n")

getSubmissions(learnpython)
getSubmissions(python, True)
getSubmissions(learnprogramming)