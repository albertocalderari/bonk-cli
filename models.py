import base64
from pathlib import Path
from typing import TypeVar, Generic

from adt import adt, Case
from pydantic import BaseModel, validator


class Config(BaseModel):
    consumer_key: str
    consumer_secret: str
    access_token: str
    access_token_secret: str
    meme_folder: Path

T = TypeVar('T')

@adt
class Option(Generic[T]):
    SOME: Case[T]
    NONE: Case[None]