from dataclasses import field
from enum import Enum
from pathlib import Path
from typing import TypeVar, Generic, Dict

from adt import adt, Case
from pydantic import BaseModel


class Config(BaseModel):
    consumer_key: str
    consumer_secret: str
    access_token: str
    access_token_secret: str
    meme_folder: Path
    category_score: Dict[str, int] = dict()


T = TypeVar('T')


@adt
class Option(Generic[T]):
    SOME: Case[T]
    NONE: Case[None]


class By(Enum):
    recent = 'recent'
    popular = 'popular'
    mixed = 'mixed'
