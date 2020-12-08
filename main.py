import os
from dotenv import load_dotenv

from image_tools import download_img
from xkcd_tools import *
from vk_tools import *


def postComics(token, group_id):
    comics_info = getRandomComicsInfo()
    comics_img = 'comics{}.png'.format(comics_info['num'])
    download_img(comics_info['img'], comics_img)
    wall_upload_info = getWallUpload(token, group_id)
    upload_result = uploadFile(
        comics_img, wall_upload_info['response']['upload_url']
    )
    save_result = saveWallPhoto(token, group_id, upload_result)
    post_result = postPhoto(
        token, -int(group_id), save_result, comics_info['alt']
    )
    try: 
        os.remove(comics_img)
    except : 
        print(f'File {comics_img} can not be removed')


def main():
    load_dotenv()
    vk_token = os.getenv('VK_TOKEN')
    vk_group_id = os.getenv('VK_GROUP_ID')
    url = 'https://api.vk.com/method/groups.get'
    postComics(vk_token, vk_group_id)


if __name__ == '__main__':
    main()
