from pathlib import Path

import pytest as pytest


@pytest.fixture
def resources_folder():
    return Path(__file__).parent / "resources"


@pytest.fixture
def fake_meme_folder(resources_folder):
    return resources_folder / "fake_memes"
