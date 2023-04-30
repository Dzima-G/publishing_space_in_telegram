import requests
import os
from helper_scripts import image_folder_name


def get_image_nasa_epic(nasa_epic_url, nasa_token, write_folder_path):
    payload = {'api_key': nasa_token}
    response_nasa_epic = requests.get(nasa_epic_url, params=payload)
    response_nasa_epic.raise_for_status()
    for i, epic_item in enumerate(response_nasa_epic.json()):
        if i <= 10:
            item_epic_data = epic_item['date'].split()[0].replace('-', '/')
            item_epic_name_image = epic_item['image']
            nasa_epic_uri = f'https://api.nasa.gov/EPIC/archive/natural/{item_epic_data}/png/{item_epic_name_image}.png'
            response_nasa_epic = requests.get(nasa_epic_uri, params=payload)
            response_nasa_epic.raise_for_status()
            image_name = f'nasa_epic_{i}.png'
            file_path = os.path.join(write_folder_path, image_name)
            with open(file_path, 'wb') as file:
                file.write(response_nasa_epic.content)


if __name__ == "__main__":
    nasa_epic_url = 'https://epic.gsfc.nasa.gov/api/natural/'
    nasa_token = os.environ['NASA_TOKEN']
    os.makedirs(image_folder_name, exist_ok=True)

    try:
        get_image_nasa_epic(nasa_epic_url, nasa_token, image_folder_name)
    except requests.exceptions.HTTPError:
        print('Ошибка! Некорректная ссылка')
