"""This module is for getting bot token from .env file."""
import os
from dotenv import load_dotenv

load_dotenv()


class Token:
    QASE_TOKEN = os.getenv('TOKEN')
