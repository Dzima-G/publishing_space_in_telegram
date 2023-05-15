import os
import time
import random
import argparse
from dotenv import load_dotenv
from helper_scripts import IMAGE_FOLDER_NAME, publish_an_image
from telegram.error import RetryAfter, NetworkError


def take_files(directory, publication_delay, telegram_token, telegram_chat_id):
    files_in_dir = os.listdir(directory)
    retry_delay = 10
    while True:
        try:
            for files_in_dirs in files_in_dir:
                path = os.path.join(files_in_dirs)
                publish_an_image(directory, path, telegram_token, telegram_chat_id)
                time.sleep(publication_delay)
            random.shuffle(files_in_dir)
        except (NetworkError, RetryAfter):
            print('Не удалось установиться соединение с сервером! Повторим попытку через 10 секунд ожидайте.')
            time.sleep(retry_delay)


if __name__ == "__main__":
    load_dotenv()
    telegram_token = os.environ['TELEGRAM_TOKEN']
    telegram_chat_id = os.environ['TELEGRAM_CHAT_ID']
    default_publication_delay = os.getenv('TELEGRAM_PUBLICATION_DELAY', default=14400)
    parser_telegram_post = argparse.ArgumentParser(description='Введите время задержки между публикациями в секундах:')
    parser_telegram_post.add_argument('publication_delay', type=int, nargs='?', default=default_publication_delay,
                                      help='Время задержки между публикациями в секундах')
    publication_delay = parser_telegram_post.parse_args().publication_delay

    take_files(IMAGE_FOLDER_NAME, publication_delay, telegram_token, telegram_chat_id)
