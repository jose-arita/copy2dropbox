import os

from dotenv import load_dotenv


load_dotenv()

DEBUG = os.getenv("DEBUG")

DROPBOX_TOKEN = os.getenv("DROPBOX_TOKEN")

DROPBOX_DIR = os.getenv("DROPBOX_DIR")

LOCAL_DIR = os.getenv("LOCAL_DIR")
