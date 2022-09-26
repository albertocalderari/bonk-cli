from argparse import Namespace

from actions.utils import search_tweets, authenticate, bonk
from models import Config
from static import CONFIG_FILE


def search(ns: Namespace):
    keywords = ns.keyword
    config = Config.parse_file(CONFIG_FILE)
    twitter = authenticate(config)
    search_tweets(twitter, keywords, config.meme_folder, bonk)
