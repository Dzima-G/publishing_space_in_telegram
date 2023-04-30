import requests
import os
from urllib.parse import urlparse, unquote
from helper_scripts import image_folder_name, getting_an_extension, get_response_api, save_image
from dotenv import load_dotenv


def download_image_nasa(nasa_token):
    nasa_url = 'https://api.nasa.gov/planetary/apod'
    payload = {'api_key': nasa_token,
               'count': '30',
               }

    for i, item_uri in enumerate(get_response_api(nasa_url, payload).json()):
        uri = item_uri['url']
        if len(getting_an_extension(uri)) > 0:
            image_name = f'nasa_apod_{i}{getting_an_extension(uri)}'
            parse_result = urlparse(uri)
            unquote_uri = unquote(f'{parse_result.scheme}://{parse_result.netloc}{parse_result.path}')
            save_image(get_response_api(unquote_uri), image_name, image_folder_name)


if __name__ == "__main__":
    load_dotenv()
    nasa_token = os.environ['NASA_TOKEN']
    os.makedirs(image_folder_name, exist_ok=True)

    try:
        download_image_nasa(nasa_token)
    except requests.exceptions.HTTPError:
        print('Ошибка! Некорректная ссылка')
