import requests
import os


def download_img(url, filename):
    response = requests.get(url)
    response.raise_for_status()
    #os.makedirs(os.path.dirname(filename), exist_ok=True)
    with open(filename, 'wb') as file:
        file.write(response.content)
