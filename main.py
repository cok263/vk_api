import os
from dotenv import load_dotenv

from image_tools import download_img
import xkcd_tools
import vk_tools


def post_comics(token, group_id):
    comics_info = xkcd_tools.get_random_comics_info()
    comics_img = 'comics{}.png'.format(comics_info['num'])
    download_img(comics_info['img'], comics_img)
    wall_upload_info = vk_tools.get_wall_upload(token, group_id)
    upload_result = vk_tools.upload_file(
        comics_img, wall_upload_info['upload_url']
    )
    save_result = vk_tools.save_wall_photo(token, group_id, upload_result)
    post_result = vk_tools.post_photo(
        token, -int(group_id), save_result, comics_info['alt']
    )
    try:
        os.remove(comics_img)
    except OSError as e:
        print(f'File {comics_img} can not be removed. Error: {e.strerror}.')


def main():
    load_dotenv()
    vk_token = os.getenv('VK_TOKEN')
    vk_group_id = os.getenv('VK_GROUP_ID')
    try:
        post_comics(vk_token, vk_group_id)
        print('Комикс опубликован на стене.')
    except Exception as e:
        print(e)


if __name__ == '__main__':
    main()
