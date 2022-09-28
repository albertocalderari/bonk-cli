from argparse import Namespace
from pathlib import Path

from actions.utils import search_tweets, authenticate, bonk
from models import Config


def search(ns: Namespace, config_folder: Path):
    keywords = ns.keyword
    config = Config.parse_file(config_folder)
    twitter = authenticate(config)
    search_tweets(twitter, keywords, config.meme_folder, bonk)
