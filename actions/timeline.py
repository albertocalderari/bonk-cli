from argparse import Namespace
from random import randint

from tweepy import OAuthHandler, API
from tweepy.models import Status

from models import Config
from static import CONFIG_FILE


def search(args: Namespace):
    config = Config.parse_file(CONFIG_FILE)
    auth = OAuthHandler(
        consumer_key=config.consumer_key,
        consumer_secret=config.consumer_secret,
        access_token=config.access_token,
        access_token_secret=config.access_token_secret
    )
    twitter = API(auth)
    keywords = " ".join(args.keyword)
    tweets = twitter.search_tweets(keywords, lang='en')
    memes = [m for m in config.meme_folder.iterdir()]
    print(f"Found {len(memes)} memes")
    for tweet in tweets:
        tweet: Status = tweet
        meme_id = randint(0, len(memes)-1)
        selected_meme = memes[meme_id]
        print(f"Tweet text:\n{tweet.text}")
        bonk = input("Shall we bonk? [any key=Yes/enter=No]")
        if bonk:
            txt = input("Add any text here: ") or ''
            _ = twitter.update_status_with_media(
                status=txt,
                filename=selected_meme,
                in_reply_to_status_id=tweet.id
            )
            u = tweet.user
            print(f"@{u.screen_name} was bonked")