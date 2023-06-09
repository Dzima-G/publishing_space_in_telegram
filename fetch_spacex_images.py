import requests
import os
import argparse
from helper_scripts import IMAGE_FOLDER_NAME, get_extension, get_response_api, save_image


def download_spacex_launch_image(launch_id):
    spacex_uri = f'https://api.spacexdata.com/v5/launches/{launch_id}'
    for i, item_uri in enumerate(get_response_api(spacex_uri).json()['links']['flickr']['original'], 1):
        image_name = f'spacex{i}{get_extension(item_uri)}'
        save_image(get_response_api(item_uri), image_name, IMAGE_FOLDER_NAME)


if __name__ == "__main__":
    parser_spacex = argparse.ArgumentParser(description='Введите ID запуска, например 61eefaa89eb1064137a1bd73')
    parser_spacex.add_argument('launch_id', nargs='?', default='61eefaa89eb1064137a1bd73', help='ID запуска')
    launch_id = parser_spacex.parse_args().launch_id
    os.makedirs(IMAGE_FOLDER_NAME, exist_ok=True)

    try:
        download_spacex_launch_image(launch_id)
    except requests.exceptions.HTTPError:
        print('Ошибка! Некорректная ссылка')
