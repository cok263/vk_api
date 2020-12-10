import requests


def get_vk_request(req, payload):
    url = f'https://api.vk.com/method/{req}'
    response = requests.post(url, data=payload)
    response.raise_for_status()
    answer_json = response.json()
    if 'response' in answer_json:
        return answer_json['response']
    raise Exception(answer_json['error']['error_msg'])


def get_wall_upload(vk_token, group_id):
    payload = {
        'access_token': vk_token,
        'v': '5.126',
        'group_id': group_id,
    }
    return get_vk_request('photos.getWallUploadServer', payload)


def upload_file(filename, url):
    with open(filename, 'rb') as file:
        files = {
            'photo': file,
        }
        response = requests.post(url, files=files)
        response.raise_for_status()
        return response.json()


def save_wall_photo(token, group_id, photo_info):
    payload = {
        'access_token': token,
        'v': '5.126',
        'group_id': group_id,
        'photo': photo_info['photo'],
        'server': photo_info['server'],
        'hash': photo_info['hash'],
    }
    return get_vk_request('photos.saveWallPhoto', payload)


def post_photo(token, owner_id, save_result, message, from_group=0):
    payload = {
        'access_token': token,
        'v': '5.126',
        'owner_id': owner_id,
        'from_group': from_group,
        'attachment': get_attachment(save_result),
        'message': message,
    }
    return get_vk_request('wall.post', payload)


def get_attachment(save_wall_photo_answer):
    response = save_wall_photo_answer[0]
    return 'photo{}_{}'.format(
        response['owner_id'],
        response['id']
    )
