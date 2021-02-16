from dotenv import load_dotenv, find_dotenv
import os

load_dotenv()

BLOCKET_URL = os.getenv("BLOCKET_URL")
BLOCKET_SEARCH_PARAMS = os.getenv("BLOCKET_SEARCH_PARAMS")
DISC_URL = os.getenv("DISC_URL")