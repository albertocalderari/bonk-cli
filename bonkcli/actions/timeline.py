from argparse import Namespace
from pathlib import Path

from bonkcli.actions.utils import search_tweets, authenticate, bonk
from bonkcli.models import Config


def search(ns: Namespace, config_file: Path):
    keywords = ns.keyword
    config = Config.parse_file(config_file)
    twitter = authenticate(config)
    search_tweets(twitter, keywords, config.meme_folder, bonk, ns.by)
