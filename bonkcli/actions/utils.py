from pathlib import Path
from random import randint
from textwrap import wrap
from typing import List, Dict, Optional

import inquirer
import tweepy
from tweepy import API, OAuthHandler
from tweepy.models import Status

from bonkcli.models import Config, By


def authenticate(config: Config) -> API:
    auth = OAuthHandler(
        consumer_key=config.consumer_key,
        consumer_secret=config.consumer_secret,
        access_token=config.access_token,
        access_token_secret=config.access_token_secret
    )
    return API(auth, wait_on_rate_limit=True)


def search_tweets(
        twitter: API,
        keywords: List[str],
        meme_folder: Path,
        category_score: Dict[str, int],
        process_tweet_callable: callable,
        by: By
):
    keywords = " ".join(keywords)
    print(f"looking for tweets matching '{keywords}'")
    cursor = twitter.search_tweets(keywords, lang='en', result_type=by.value, tweet_mode='extended', count=100)
    while True:
        for tweet in cursor:
            process_tweet_callable(meme_folder=meme_folder, category_score=category_score, tweet=tweet, twitter=twitter)
        cursor = twitter.search_tweets(
            keywords,
            max_id=cursor.max_id,
            lang='en',
            result_type='recent',
            tweet_mode='extended',
            count=200)
        if not cursor:
            break


def get_meme(meme_folder: Path) -> Path:
    memes = [m for m in meme_folder.iterdir()]
    print(f"Found {len(memes)} memes\n")
    meme_id = randint(0, len(memes) - 1)
    selected_meme = memes[meme_id]
    return selected_meme


def bonk(meme_folder: Path, category_score: Dict[str, int], tweet: Status, twitter: API):
    tweet: Status = tweet
    print("\n---------------------------------------\n")
    print(f"Author: @{tweet.author.screen_name}")
    if hasattr(tweet, 'retweeted_status'):
        full_text = tweet.retweeted_status.full_text
    else:
        full_text = tweet.full_text
    print(f"Tweet text:\n{wrap_text(full_text)}")
    bonk = input("Shall we bonk? [any key=Yes/enter=No] ")
    if bonk:
        meme_sub_folder = chose_memes_folder(meme_folder, category_score)
        selected_meme = get_meme(meme_sub_folder)
        txt = input("Add any text here: ") or ''
        try:
            _ = twitter.update_status_with_media(
                status=txt,
                filename=selected_meme,
                in_reply_to_status_id=tweet.id,
                auto_populate_reply_metadata=True
            )
            u = tweet.user
            print(f"@{u.screen_name} was bonked")
        except tweepy.errors.Forbidden as e:
            print(f"\nERROR: Could not bonk because of an error: {e}")


def wrap_text(text: str) -> str:
    return '\n'.join(wrap(text, 70))


def chose_memes_folder(meme_folder: Path, category_score: Dict[str, int]) -> Path:
    categories = build_and_sort_categories(category_score, meme_folder)

    questions = [
        inquirer.List(
            'meme',
            message="Wich memes do you want to use?",
            choices=categories,
        )
    ]
    prompt_result: Optional[Dict] = inquirer.prompt(questions)

    if prompt_result:
        sub_folder = prompt_result['meme']
        category_score[sub_folder] += 1
    else:
        raise KeyboardInterrupt("Cancelled by user")
    return meme_folder / sub_folder


def build_and_sort_categories(category_score, meme_folder):
    categories = []
    for category in meme_folder.iterdir():
        if category.name.startswith('.'):
            continue
        if category.name not in category_score:
            category_score[category.name] = 0
        categories.append(category.name)
    categories.sort(key=category_score.get, reverse=True)
    return categories
