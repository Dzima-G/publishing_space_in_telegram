import telegram
import os
import random
import argparse
from dotenv import load_dotenv
from helper_scripts import image_folder_name


def publish_image(directory, telegram_token, image):
    bot = telegram.Bot(token=telegram_token)
    file = os.path.join(str(directory), image)
    bot.send_photo(chat_id='-1001906233310', photo=open(file, 'rb'))


if __name__ == "__main__":
    load_dotenv()
    telegram_token = os.environ['TELEGRAM_TOKEN']
    files_in_dir = os.listdir(image_folder_name)
    parser_post_telegram = argparse.ArgumentParser(description='Введите название файла изображения')
    parser_post_telegram.add_argument('image_file_name', nargs='?', default=random.choice(files_in_dir),
                                      help='Введите название файла картинки из папки images')
    image_file_name = parser_post_telegram.parse_args().image_file_name

    try:
        publish_image(image_folder_name, telegram_token, image_file_name)
    except FileExistsError:
        pass
