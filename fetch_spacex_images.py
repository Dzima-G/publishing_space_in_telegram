import requests
import os
import argparse
from helper_scripts import getting_an_extension
from helper_scripts import image_folder_name
from pprint import pprint


def fetch_spacex_last_launch(one_launch_url, write_folder_path):
    response_one_launch = requests.get(one_launch_url)
    response_one_launch.raise_for_status()
    for i, item_uri in enumerate(response_one_launch.json()['links']['flickr']['original']):
        image_name = f'spacex{i}{getting_an_extension(item_uri)}'
        response_image = requests.get(item_uri)
        response_image.raise_for_status()
        file_path = os.path.join(write_folder_path, image_name)
        with open(file_path, 'wb') as file:
            file.write(response_image.content)


if __name__ == "__main__":
    parser_spacex = argparse.ArgumentParser(description='Введите ID запуска')
    parser_spacex.add_argument('id_launch', nargs='?', default='61eefaa89eb1064137a1bd73', help='ID запуска')
    launch_id = parser_spacex.parse_args().id_launch
    spacex_uri = f'https://api.spacexdata.com/v5/launches/{launch_id}'
    os.makedirs(image_folder_name, exist_ok=True)

    try:
        fetch_spacex_last_launch(spacex_uri, image_folder_name)
    except requests.exceptions.HTTPError:
        print('Ошибка! Некорректная ссылка')
