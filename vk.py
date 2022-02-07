import json
import os

import requests


def naming(n, num_list):  # сделано, для файлов с одинаковым названием
    if n in num_list:
        n *= 10
        naming(n, num_list)
        return naming(n, num_list)
    else:
        return n


# with open('token.txt', 'r') as f:  #рядом с файлами можно положить текстовый файл, первая строка - токен ВК
#     VKTOKEN = f.readline().strip()


class Vk:

    def __init__(self, token):
        self.token = token
        self.data = []
        self.namelist = []
        self.img_height_width_dict = {}

    URL = 'https://api.vk.com/method/photos.get'
    params = {
        'owner_id': input('Введите id пользователя ВК: '),
        'access_token': '',  # vk token
        'album_id': 'profile',
        'extended': 1,
        'photo_sizes': 1,
        'count': '100',
        'rev': 0,
        'v': '5.131'
    }

    def get_img_with_params(self):
        res = requests.get(Vk.URL, params=Vk.params)
        r = res.json()
        order_number = 0
        if not os.path.isdir('images'):
            os.mkdir('images')
        for v in r.values():
            for key, value in v.items():
                if key == 'items':
                    for _ in value:
                        img = r['response']['items'][order_number]['sizes'][-1]['url']
                        img_likes_count = r['response']['items'][order_number]['likes']['count']
                        img_size = r['response']['items'][order_number]['sizes'][-1]['type']
                        img_size_h = r['response']['items'][order_number]['sizes'][-1]['height']
                        img_size_w = r['response']['items'][order_number]['sizes'][-1]['width']
                        p = requests.get(img)
                        img_name = naming(img_likes_count, self.namelist)
                        img_hw = {'height': img_size_h, 'width': img_size_w}
                        self.img_height_width_dict[img_name] = img_hw
                        self.namelist.append(img_name)
                        out = open(f'images\\{img_name}.jpg', 'wb')
                        out.write(p.content)
                        out.close()
                        data_dict = {'filename': f'{img_name}.jpg', 'size': f'{img_size}'}
                        self.data.append(data_dict)
                        with open(f'images\\{img_name}.txt', 'w') as img_file:
                            json.dump(self.data, img_file)
                        self.data.clear()
                        data_dict.clear()
                        order_number += 1
