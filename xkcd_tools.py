import requests
import random


def get_comics_info(id):
    url = 'http://xkcd.com/{}/info.0.json'.format(id)
    response = requests.get(url)
    response.raise_for_status()
    return response.json()


def get_last_comics_info():
    response = requests.get('http://xkcd.com/info.0.json')
    response.raise_for_status()
    return response.json()


def get_random_comics_info():
    comics_count = get_last_comics_info()['num']
    random.seed()
    return get_comics_info(random.randint(1, comics_count))
