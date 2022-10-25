from pathlib import Path
from random import randint
from textwrap import wrap
from typing import List

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


def search_tweets(twitter: API, keywords: List[str], meme_folder: Path, process_tweet_callable: callable, by: By):
    keywords = " ".join(keywords)
    memes = get_memes(meme_folder)
    print(f"looking for tweets matching '{keywords}'")
    cursor = twitter.search_tweets(keywords, lang='en', result_type=by.value, tweet_mode='extended', count=100)
    while True:
        for tweet in cursor:
            process_tweet_callable(memes=memes, tweet=tweet, twitter=twitter)
        cursor = twitter.search_tweets(
            keywords,
            max_id=cursor.max_id,
            lang='en',
            result_type='recent',
            tweet_mode='extended',
            count=200)
        if not cursor:
            break


def get_memes(meme_folder):
    memes = [m for m in meme_folder.iterdir()]
    print(f"Found {len(memes)} memes\n")
    return memes


def bonk(memes: List[str], tweet: Status, twitter: API):
    tweet: Status = tweet
    meme_id = randint(0, len(memes) - 1)
    selected_meme = memes[meme_id]
    print("\n---------------------------------------\n")
    print(f"Author: @{tweet.author.screen_name}")
    print(f"Tweet text:\n{wrap_text(tweet.full_text)}")
    bonk = input("Shall we bonk? [any key=Yes/enter=No] ")
    if bonk:
        txt = input("Add any text here: ") or ''
        _ = twitter.update_status_with_media(
            status=txt,
            filename=selected_meme,
            in_reply_to_status_id=tweet.id,
            auto_populate_reply_metadata=True
        )
        u = tweet.user
        print(f"@{u.screen_name} was bonked")


def wrap_text(text: str) -> str:
    return '\n'.join(wrap(text, 70))
