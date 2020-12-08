import requests


def getVkRequest(req, payload):
    url = f'https://api.vk.com/method/{req}'
    response = requests.post(url, data=payload)
    response.raise_for_status()
    return response.json()


def getWallUpload(vk_token, group_id):
    payload = {
        'access_token': vk_token,
        'v': '5.126',
        'group_id': group_id,
    }
    return getVkRequest('photos.getWallUploadServer', payload)


def uploadFile(filename, url):
    with open(filename, 'rb') as file:
        files = {
            'photo': file,
        }
        response = requests.post(url, files=files)
        response.raise_for_status()
        return response.json()


def saveWallPhoto(token, group_id, photo_info):
    payload = {
        'access_token': token,
        'v': '5.126',
        'group_id': group_id,
        'photo': photo_info['photo'],
        'server': photo_info['server'],
        'hash': photo_info['hash'],
    }
    return getVkRequest('photos.saveWallPhoto', payload)


def postPhoto(token, owner_id, save_result, message, from_group=0):
    payload = {
        'access_token': token,
        'v': '5.126',
        'owner_id': owner_id,
        'from_group': from_group,
        'attachment': getAttachment(save_result),
        'message': message,
    }
    return getVkRequest('wall.post', payload)


def getAttachment(save_wall_photo_answer):
    response = save_wall_photo_answer['response'][0]
    return 'photo{}_{}'.format(
        response['owner_id'],
        response['id']
    )
