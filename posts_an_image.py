import telegram
import os
import random
import argparse
from dotenv import load_dotenv
from helper_scripts import image_folder_name, publishes_an_image


def publish_image(directory, telegram_token, telegram_chat_id, image):
    bot = telegram.Bot(token=telegram_token)
    publishes_an_image(directory, image, bot, telegram_chat_id)


if __name__ == "__main__":
    load_dotenv()
    telegram_token = os.environ['TELEGRAM_TOKEN']
    telegram_chat_id = os.environ['TG_CHAT_ID']
    files_in_dir = os.listdir(image_folder_name)
    parser_post_telegram = argparse.ArgumentParser(description='Имя файла изображения')
    parser_post_telegram.add_argument('image_file_name', nargs='?', default=random.choice(files_in_dir),
                                      help='Введите имя файла изображения из папки images')
    image_file_name = parser_post_telegram.parse_args().image_file_name

    publish_image(image_folder_name, telegram_token, telegram_chat_id, image_file_name)
