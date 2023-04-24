import os
from urllib.parse import urlparse
from dotenv import load_dotenv


def getting_an_extension(uri):
    extension = urlparse(uri).path
    return os.path.splitext(extension)[1]


load_dotenv()
image_folder_name = 'images'
token_telegram = os.environ['TELEGRAM_TOKEN']
