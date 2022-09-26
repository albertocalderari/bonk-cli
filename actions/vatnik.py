from argparse import Namespace
from textwrap import wrap

import tweepy
from tweepy import API
from tweepy.models import Status

from actions.utils import authenticate, search_tweets, wrap_text, bonk, get_memes
from models import Config
from static import CONFIG_FILE

seen = set()


def get_user(tweet: Status, **__):
    author = tweet.author
    handle = author.screen_name
    if handle not in seen:
        print("\n---------------------------------------\n")
        print(f"User: @{handle}")
        description = wrap_text(author)
        print(f"Bio: '{description}'")
        print(f"Profile Url: 'https://twitter.com/{handle}'")
        seen.add(handle)


def search(ns: Namespace):
    keywords = ns.keyword
    config = Config.parse_file(CONFIG_FILE)
    twitter = authenticate(config)
    search_tweets(twitter, keywords, config.meme_folder, get_user)


def bonk_vatnik(ns: Namespace):
    user = ns.user
    count = ns.n
    config = Config.parse_file(CONFIG_FILE)
    twitter: API = authenticate(config)
    cursor = tweepy.Cursor(twitter.user_timeline, creen_name=user, count=count, include_rts=False, tweet_mode='extended')
    memes = get_memes(config.meme_folder)
    for tweet in cursor.items():
        bonk(memes, tweet, twitter)

