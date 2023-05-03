import os
import requests
from urllib.parse import urlparse


def get_extension(uri):
    extension = urlparse(uri).path
    return os.path.splitext(extension)[1]


def get_response_api(api_url, *get_payload):
    if not get_payload:
        payload = {}
    else:
        payload = get_payload[0]
    response = requests.get(api_url, params=payload)
    response.raise_for_status()
    return response


def save_image(file_image, image_name, image_folder_name):
    file_path = os.path.join(image_folder_name, image_name)
    with open(file_path, 'wb') as file:
        file.write(file_image.content)


image_folder_name = 'images'
