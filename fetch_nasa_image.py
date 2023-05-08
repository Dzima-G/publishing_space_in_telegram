import requests
import os
from urllib.parse import urlparse, unquote
from helper_scripts import IMAGE_FOLDER_NAME, get_extension, get_response_api, save_image
from dotenv import load_dotenv


def download_image_nasa(nasa_token, images_conut):
    nasa_url = 'https://api.nasa.gov/planetary/apod'
    payload = {'api_key': nasa_token,
               'count': images_conut,
               }
    for i, item_uri in enumerate(get_response_api(nasa_url, payload).json()):
        if not item_uri['media_type'] == 'image':
            continue
        uri = item_uri['url']
        if not get_extension(uri):
            continue
        image_name = f'nasa_apod_{i + 1}{get_extension(uri)}'
        parse_result = urlparse(uri)
        unquote_uri = unquote(f'{parse_result.scheme}://{parse_result.netloc}{parse_result.path}')
        save_image(get_response_api(unquote_uri), image_name, IMAGE_FOLDER_NAME)


if __name__ == "__main__":
    load_dotenv()
    nasa_token = os.environ['NASA_TOKEN']
    nasa_images_count = os.environ['NASA_IMAGES_COUNT']
    os.makedirs(IMAGE_FOLDER_NAME, exist_ok=True)

    try:
        download_image_nasa(nasa_token, nasa_images_count)
    except requests.exceptions.HTTPError:
        print('Ошибка! Некорректная ссылка')
