import telegram
import os
import time
import random
import argparse
from dotenv import load_dotenv
from helper_scripts import image_folder_name, publishes_an_image
from telegram.error import RetryAfter, TimedOut, NetworkError


def take_files(directory, publication_delay, telegram_token, telegram_chat_id):
    files_in_dir = os.listdir(directory)
    retry_delay = 10
    while True:
        try:
            bot = telegram.Bot(token=telegram_token)
            for files_in_dirs in files_in_dir:
                path = os.path.join(files_in_dirs)
                publishes_an_image(directory, path, bot, telegram_chat_id)
                time.sleep(publication_delay)
            random.shuffle(files_in_dir)
        except (NetworkError, RetryAfter) as q:
            print('Не удалось установиться соединение с сервером! Повторим попытку через 10 секунд ожидайте.')
            time.sleep(retry_delay)


if __name__ == "__main__":
    load_dotenv()
    telegram_token = os.environ['TELEGRAM_TOKEN']
    telegram_chat_id = os.environ['TG_CHAT_ID']
    publication_delay_default = os.environ['PUBLICATION_DELAY_TELEGRAM']
    parser_post_telegram = argparse.ArgumentParser(description='Введите время задержки между публикациями в секундах:')
    parser_post_telegram.add_argument('publication_delay', type=int, nargs='?', default=publication_delay_default,
                                      help='Время задержки между публикациями в секундах')
    publication_delay = parser_post_telegram.parse_args().publication_delay

    take_files(image_folder_name, publication_delay, telegram_token, telegram_chat_id)
