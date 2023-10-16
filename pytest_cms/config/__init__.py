import os


__all___ = [
    'SETTING_YMAL_DIR'
]

BASE_URL = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

SETTING_YMAL_DIR = os.path.join(BASE_URL, "config")