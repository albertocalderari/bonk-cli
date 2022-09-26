from random import randint
from time import sleep

from tweepy import API, OAuthHandler

from models import Config
from static import CONFIG_FILE


def init():
    consumer_key = input("Please enter your API Key: ")
    consumer_secret = input("Please enter your Twitter password: ")
    access_token = input("Please enter your Bearer Token: ")
    meme_folder = input("Please paste the path to your memes folder: ").strip()
    conf = Config(
        consumer_key=consumer_key,
        consumer_secret=consumer_secret,
        access_token=access_token,
        meme_folder=meme_folder
    )
    with CONFIG_FILE.open('w') as f:
        f.write(conf.json())


def search():
    config = Config.parse_file(CONFIG_FILE)
    auth = OAuthHandler(
        consumer_key=config.consumer_key,
        consumer_secret=config.consumer_secret,
        access_token=config.access_token,
        access_token_secret=config.access_token_secret
    )
    twitter = API(auth)
    tweets = twitter.search_tweets("ukronazi", lang='en')

    memes = [m for m in config.meme_folder.iterdir()]
    print(f"Found {len(memes)} memes")
    for tweet in tweets:
        meme_id = randint(0, len(memes))
        selected_meme = memes[meme_id]
        tweet = twitter.update_status_with_media(status='', filename=selected_meme, in_reply_to_status_id=tweet.id,
                                                 auto_populate_reply_metadata=True)
        print(f"Tweeted {tweet}")
        sleep(randint(1, 20))
