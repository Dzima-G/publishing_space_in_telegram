import requests
import os
import argparse
from helper_scripts import getting_an_extension
from helper_scripts import image_folder_name
from pprint import pprint


def fetch_spacex_last_launch(url_one_launch, write_folder_path):
    response_one_launch = requests.get(url_one_launch)
    response_one_launch.raise_for_status()
    for i, uri_item in enumerate(response_one_launch.json()['links']['flickr']['original']):
        image_name = f'spacex{i}{getting_an_extension(uri_item)}'
        response_image = requests.get(uri_item)
        response_image.raise_for_status()
        file_path = os.path.join(write_folder_path, image_name)
        with open(file_path, 'wb') as file:
            file.write(response_image.content)


if __name__ == "__main__":
    parser_spacex = argparse.ArgumentParser(description='Введите ID запуска')
    parser_spacex.add_argument('id_launch', nargs='?', default='61eefaa89eb1064137a1bd73', help='ID запуска')
    id_launch = parser_spacex.parse_args().id_launch
    url_spacex = f'https://api.spacexdata.com/v5/launches/{id_launch}'

    try:
        os.makedirs(image_folder_name)
    except FileExistsError:
        pass

    try:
        fetch_spacex_last_launch(url_spacex, image_folder_name)
    except requests.exceptions.HTTPError:
        print('Ошибка! Некорректная ссылка')
