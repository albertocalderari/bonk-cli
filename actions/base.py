from argparse import Namespace
from pathlib import Path

from models import Config, Option
from static import CONFIG_FILE


def init(args: Namespace):
    current_config = get_current_config(CONFIG_FILE)
    [
        current_consumer_key,
        current_consumer_secret,
        current_access_token,
        current_access_token_secret,
        current_meme_folder
    ] = current_config.match(
        some=lambda c: [c.consumer_key, c.consumer_secret, c.access_token, c.access_token_secret, c.meme_folder],
        none=lambda: [None, None, None, None, None]
    )
    consumer_key = input_request('consumer_key', current_consumer_key)
    consumer_secret = input_request('consumer_secret', current_consumer_secret)
    access_token = input_request('access_token', current_access_token)
    access_token_secret = input_request('access_token_secret', current_access_token_secret)
    meme_folder = input_request('meme_folder', current_meme_folder)
    conf = Config(
        consumer_key=consumer_key,
        consumer_secret=consumer_secret,
        access_token=access_token,
        access_token_secret=access_token_secret,
        meme_folder=meme_folder
    )
    with CONFIG_FILE.open('w') as f:
        f.write(conf.json())


def input_request(key, current) -> str:
    key_str = ' '.join(key.split('_'))
    value = input(f"Please enter your '{key_str}' [{current}]: ").strip()
    return value or current


def get_current_config(config_file: Path) -> Option[Config]:
    if config_file.exists():
        return Option.SOME(Config.parse_file(config_file))
    else:
        return Option.NONE()
