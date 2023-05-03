import requests
import os
from helper_scripts import image_folder_name, get_response_api, save_image
from dotenv import load_dotenv
from datetime import datetime


def download_image_nasa_epic(nasa_token, images_count):
    nasa_epic_url = 'https://epic.gsfc.nasa.gov/api/natural/'
    payload = {'api_key': nasa_token}
    for i, epic_item in enumerate(get_response_api(nasa_epic_url, payload).json()):
        if i < int(images_count):
            item_epic_data = datetime.fromisoformat(epic_item['date']).strftime("%Y/%m/%d")
            item_epic_name_image = epic_item['image']
            nasa_epic_uri = f'https://api.nasa.gov/EPIC/archive/natural/{item_epic_data}/png/{item_epic_name_image}.png'
            image_name = f'nasa_epic_{i + 1}.png'
            save_image(get_response_api(nasa_epic_uri, payload), image_name, image_folder_name)
        else:
            break


if __name__ == "__main__":
    load_dotenv()
    nasa_token = os.environ['NASA_TOKEN']
    nasa_epic_images_count = os.environ['NASA_EPIC_IMAGES_COUNT']
    os.makedirs(image_folder_name, exist_ok=True)

    try:
        download_image_nasa_epic(nasa_token, nasa_epic_images_count)
    except requests.exceptions.HTTPError:
        print('Ошибка! Некорректная ссылка')
