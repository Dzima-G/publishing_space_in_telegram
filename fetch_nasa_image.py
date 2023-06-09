import requests
import os
from urllib.parse import urlparse, unquote
from helper_scripts import IMAGE_FOLDER_NAME, get_extension, get_response_api, save_image
from dotenv import load_dotenv


def download_image_nasa(nasa_token, images_count):
    nasa_url = 'https://api.nasa.gov/planetary/apod'
    payload = {'api_key': nasa_token,
               'count': images_count,
               }
    for i, item_uri in enumerate(get_response_api(nasa_url, payload).json(), 1):
        if not item_uri['media_type'] == 'image':
            continue
        uri = item_uri['url']
        if not get_extension(uri):
            continue
        image_name = f'nasa_apod_{i}{get_extension(uri)}'
        parsed_result = urlparse(uri)
        unquoted_uri = unquote(f'{parsed_result.scheme}://{parsed_result.netloc}{parsed_result.path}')
        save_image(get_response_api(unquoted_uri), image_name, IMAGE_FOLDER_NAME)


if __name__ == "__main__":
    load_dotenv()
    nasa_token = os.environ['NASA_TOKEN']
    nasa_images_count = os.getenv('NASA_IMAGES_COUNT', default=30)
    os.makedirs(IMAGE_FOLDER_NAME, exist_ok=True)

    try:
        download_image_nasa(nasa_token, nasa_images_count)
    except requests.exceptions.HTTPError:
        print('Ошибка! Некорректная ссылка')
