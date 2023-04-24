import telegram
import os
import time
import random
import argparse
from helper_scripts import image_folder_name, token_telegram


def take_files(directory, delay_after_publication, token_telegram):
    bot = telegram.Bot(token=token_telegram)
    files_in_dir = os.listdir(directory)

    while True:
        for files_in_dirs in files_in_dir:
            path = os.path.join(files_in_dirs)
            file = os.path.join(str(directory), path)
            bot.send_photo(chat_id='-1001906233310', photo=open(file, 'rb'))
            time.sleep(int(delay_after_publication))
        random.shuffle(files_in_dir)


if __name__ == "__main__":
    publication_delay_default = os.environ['PUBLICATION_DELAY_TELEGRAM']
    parser_post_telegram = argparse.ArgumentParser(description='Введите время задержки между публикациями в секундах:')
    parser_post_telegram.add_argument('publication_delay', nargs='?', default=publication_delay_default,
                                      help='Время задержки между публикациями в секундах')
    publication_delay = parser_post_telegram.parse_args().publication_delay

    try:
        take_files(image_folder_name, publication_delay, token_telegram)
    except FileExistsError:
        pass
