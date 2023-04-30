import os
from urllib.parse import urlparse


def getting_an_extension(uri):
    extension = urlparse(uri).path
    return os.path.splitext(extension)[1]


image_folder_name = 'images'