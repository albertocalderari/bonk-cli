import base64
from pathlib import Path

from pydantic import BaseModel, validator


class Config(BaseModel):
    consumer_key: str
    consumer_secret: str
    access_token: str
    access_token_secret: str
    meme_folder: Path
