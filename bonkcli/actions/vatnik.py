from argparse import Namespace
from pathlib import Path

from tweepy import API
from tweepy.models import Status

from bonkcli.actions.utils import authenticate, search_tweets, wrap_text, bonk, get_memes
from bonkcli.models import Config

seen = set()


def get_user(tweet: Status, **__):
    author = tweet.author
    handle = author.screen_name
    if handle not in seen:
        print("\n---------------------------------------\n")
        print(f"User: @{handle}")
        description = wrap_text(author.description)
        print(f"Bio: '{description}'")
        print(f"Profile Url: 'https://twitter.com/{handle}'")
        seen.add(handle)


def search(ns: Namespace, config_folder: Path):
    keywords = ns.keyword
    by = ns.by
    config = Config.parse_file(config_folder)
    twitter = authenticate(config)
    search_tweets(twitter, keywords, config.meme_folder, get_user, by)


def bonk_vatnik(ns: Namespace, config_file: Path):
    user = ns.user
    count = ns.n
    config = Config.parse_file(config_file)
    twitter: API = authenticate(config)
    print(f"Searching timelie of user {user}")
    cursor = twitter.user_timeline(screen_name=user, count=count, tweet_mode='extended', exclude_replies=True)
    memes = get_memes(config.meme_folder)
    for tweet in cursor:
        bonk(memes, tweet, twitter)
