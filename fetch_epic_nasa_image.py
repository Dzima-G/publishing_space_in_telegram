import requests
import os
from helper_scripts import IMAGE_FOLDER_NAME, get_response_api, save_image
from dotenv import load_dotenv
from datetime import datetime


def download_image_nasa_epic(nasa_token, images_count):
    nasa_epic_url = 'https://epic.gsfc.nasa.gov/api/natural/'
    payload = {'api_key': nasa_token}
    images_count = int(images_count)
    for i, epic_item in enumerate(get_response_api(nasa_epic_url, payload).json(), 1):
        if i >= images_count:
            break
        item_epic_data = datetime.fromisoformat(epic_item['date']).strftime("%Y/%m/%d")
        item_epic_name_image = epic_item['image']
        nasa_epic_uri = f'https://api.nasa.gov/EPIC/archive/natural/{item_epic_data}/png/{item_epic_name_image}.png'
        image_name = f'nasa_epic_{i}.png'
        save_image(get_response_api(nasa_epic_uri, payload), image_name, IMAGE_FOLDER_NAME)


if __name__ == "__main__":
    load_dotenv()
    nasa_token = os.environ['NASA_TOKEN']
    nasa_epic_images_count = os.getenv('NASA_EPIC_IMAGES_COUNT', default=10)
    os.makedirs(IMAGE_FOLDER_NAME, exist_ok=True)

    try:
        download_image_nasa_epic(nasa_token, nasa_epic_images_count)
    except requests.exceptions.HTTPError:
        print('Ошибка! Некорректная ссылка')
