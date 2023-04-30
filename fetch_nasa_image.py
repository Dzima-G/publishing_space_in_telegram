import requests
import os
from urllib.parse import urlparse, unquote
from helper_scripts import getting_an_extension
from helper_scripts import image_folder_name


def get_image_nasa(nasa_url, nasa_token, write_folder_path):
    payload = {'api_key': nasa_token,
               'count': '31',
               }
    response_nasa = requests.get(nasa_url, params=payload)
    response_nasa.raise_for_status()
    for i, item_uri in enumerate(response_nasa.json()):
        uri = item_uri['url']
        if len(getting_an_extension(uri)) > 0:
            image_name = f'nasa_apod_{i}{getting_an_extension(uri)}'
            parse_result = urlparse(uri)
            unquote_uri = unquote(f'{parse_result.scheme}://{parse_result.netloc}{parse_result.path}')
            response_image = requests.get(unquote_uri)
            response_image.raise_for_status()
            file_path = os.path.join(write_folder_path, image_name)
            with open(file_path, 'wb') as file:
                file.write(response_image.content)


if __name__ == "__main__":
    nasa_url = 'https://api.nasa.gov/planetary/apod'
    nasa_token = os.environ['NASA_TOKEN']

    try:
        os.makedirs(image_folder_name)
    except FileExistsError:
        pass

    try:
        get_image_nasa(nasa_url, nasa_token, image_folder_name)
    except requests.exceptions.HTTPError:
        print('Ошибка! Некорректная ссылка')
