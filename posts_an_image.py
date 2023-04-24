import telegram
import os
import random
import argparse
from helper_scripts import image_folder_name, token_telegram


def publish_image(directory, token_telegram, image):
    bot = telegram.Bot(token=token_telegram)
    file = os.path.join(str(directory), image)
    bot.send_photo(chat_id='-1001906233310', photo=open(file, 'rb'))


if __name__ == "__main__":
    files_in_dir = os.listdir(image_folder_name)
    parser_post_telegram = argparse.ArgumentParser(description='Введите название файла изображения')
    parser_post_telegram.add_argument('images_file_name', nargs='?', default=random.choice(files_in_dir),
                                      help='Введите название файла картинки из папки images')
    images_file_name = parser_post_telegram.parse_args().images_file_name

    try:
        publish_image(image_folder_name, token_telegram, images_file_name)
    except FileExistsError:
        pass
