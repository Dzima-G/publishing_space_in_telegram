import requests
import os
from helper_scripts import image_folder_name


def get_image_nasa_epic(url_nasa_epic, token_nasa, write_folder_path):
    payload = {'api_key': token_nasa}
    response_nasa_epic = requests.get(url_nasa_epic, params=payload)
    response_nasa_epic.raise_for_status()
    for i, item_epic in enumerate(response_nasa_epic.json()):
        if i <= 10:
            item_epic_data = item_epic['date'].split()[0].replace('-', '/')
            item_epic_name_image = item_epic['image']
            uri_nasa_epic = f'https://api.nasa.gov/EPIC/archive/natural/{item_epic_data}/png/{item_epic_name_image}.png'
            response_nasa_epic = requests.get(uri_nasa_epic, params=payload)
            response_nasa_epic.raise_for_status()
            image_name = f'nasa_epic_{i}.png'
            file_path = os.path.join(write_folder_path, image_name)
            with open(file_path, 'wb') as file:
                file.write(response_nasa_epic.content)


if __name__ == "__main__":
    url_nasa_epic = 'https://epic.gsfc.nasa.gov/api/natural/'
    token_nasa = os.environ['NASA_TOKEN']

    try:
        os.makedirs(image_folder_name)
    except FileExistsError:
        pass

    try:
        get_image_nasa_epic(url_nasa_epic, token_nasa, image_folder_name)
    except requests.exceptions.HTTPError:
        print('Ошибка! Некорректная ссылка')