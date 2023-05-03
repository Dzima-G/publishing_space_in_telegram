import requests
import os
import argparse
from helper_scripts import image_folder_name, get_extension, get_response_api, save_image


def download_spacex_launch_image(launch_id):
    spacex_uri = f'https://api.spacexdata.com/v5/launches/{launch_id}'
    for i, item_uri in enumerate(get_response_api(spacex_uri).json()['links']['flickr']['original']):
        image_name = f'spacex{i}{get_extension(item_uri)}'
        save_image(get_response_api(item_uri), image_name, image_folder_name)


if __name__ == "__main__":
    parser_spacex = argparse.ArgumentParser(description='Введите ID запуска')
    parser_spacex.add_argument('id_launch', nargs='?', default='61eefaa89eb1064137a1bd73', help='ID запуска')
    launch_id = parser_spacex.parse_args().id_launch
    os.makedirs(image_folder_name, exist_ok=True)

    try:
        download_spacex_launch_image(launch_id)
    except requests.exceptions.HTTPError:
        print('Ошибка! Некорректная ссылка')
