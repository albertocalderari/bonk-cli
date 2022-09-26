import os
from pathlib import Path

HOME_FOLDER = Path(os.getenv('HOME'))
CONFIG_FILE = HOME_FOLDER / '.bonkcli'
