import requests
import random


def getComicsInfo(id):
    url = 'http://xkcd.com/{}/info.0.json'.format(id)
    response = requests.get(url)
    response.raise_for_status()
    return response.json()


def getLastComicsInfo():
    response = requests.get('http://xkcd.com/info.0.json')
    response.raise_for_status()
    return response.json()


def getRandomComicsInfo():
    comics_count = getLastComicsInfo()['num']
    random.seed()
    return getComicsInfo(random.randint(1, comics_count))
