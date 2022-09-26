from argparse import Namespace
from textwrap import wrap

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
    config = Config.parse_file(CONFIG_FILE)
    twitter: API = authenticate(config)
    tweets = twitter.user_timeline(screen_name=user, count=100, include_rts=False)
    memes = get_memes(config.meme_folder)
    for tweet in tweets:
        bonk(memes, tweet, twitter)

