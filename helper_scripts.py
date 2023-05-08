import os
import requests
import telegram
from urllib.parse import urlparse

IMAGE_FOLDER_NAME = 'images'


def get_extension(uri):
    extension = urlparse(uri).path
    return os.path.splitext(extension)[1]


def get_response_api(api_url, payload_request=None):
    payload = payload_request
    response = requests.get(api_url, params=payload)
    response.raise_for_status()
    return response


def save_image(file_image, image_name, image_folder_name):
    file_path = os.path.join(image_folder_name, image_name)
    with open(file_path, 'wb') as file:
        file.write(file_image.content)


def publishes_an_image(directory, image_file_name, telegram_token, tg_chat_id):
    bot = telegram.Bot(token=telegram_token)
    file = os.path.join(directory, image_file_name)
    with open(file, 'rb') as file:
        bot.send_photo(chat_id=tg_chat_id, photo=file)
