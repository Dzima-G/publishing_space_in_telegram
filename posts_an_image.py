import os
import random
import argparse
from dotenv import load_dotenv
from helper_scripts import IMAGE_FOLDER_NAME, publish_an_image

if __name__ == "__main__":
    load_dotenv()
    telegram_token = os.environ['TELEGRAM_TOKEN']
    telegram_chat_id = os.environ['TELEGRAM_CHAT_ID']
    files_in_dir = os.listdir(IMAGE_FOLDER_NAME)
    parser_post_telegram = argparse.ArgumentParser(description='Имя файла изображения')
    parser_post_telegram.add_argument('image_file_name', nargs='?', default=random.choice(files_in_dir),
                                      help='Введите имя файла изображения из папки images')
    image_file_name = parser_post_telegram.parse_args().image_file_name

    publish_an_image(IMAGE_FOLDER_NAME, image_file_name, telegram_token, telegram_chat_id)
