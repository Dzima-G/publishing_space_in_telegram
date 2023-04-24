import requests
import os
from urllib.parse import urlparse, unquote
from helper_scripts import getting_an_extension
from helper_scripts import image_folder_name


def get_image_nasa(url_nasa, token_nasa, write_folder_path):
    payload = {'api_key': token_nasa,
               'count': '31',
               }
    response_nasa = requests.get(url_nasa, params=payload)
    response_nasa.raise_for_status()
    for i, uri_item in enumerate(response_nasa.json()):
        uri = uri_item['url']
        if len(getting_an_extension(uri)) > 0:
            image_name = f'nasa_apod_{i}{getting_an_extension(uri)}'
            parse_result = urlparse(uri)
            uri_unquote = unquote(f'{parse_result.scheme}://{parse_result.netloc}{parse_result.path}')
            response_image = requests.get(uri_unquote)
            response_image.raise_for_status()
            file_path = os.path.join(write_folder_path, image_name)
            with open(file_path, 'wb') as file:
                file.write(response_image.content)


if __name__ == "__main__":
    url_nasa = 'https://api.nasa.gov/planetary/apod'
    token_nasa = os.environ['NASA_TOKEN']

    try:
        os.makedirs(image_folder_name)
    except FileExistsError:
        pass

    try:
        get_image_nasa(url_nasa, token_nasa, image_folder_name)
    except requests.exceptions.HTTPError:
        print('Ошибка! Некорректная ссылка')
