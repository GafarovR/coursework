import json

import requests


def naming(n, num_list):  # сделано, для файлов с одинаковым названием
    if n in num_list:
        n *= 10
        naming(n, num_list)
        return naming(n, num_list)
    else:
        return n


class Vk:

    def __init__(self):
        self.token = ''       # vk token
        self.data = []
        self.namelist = []
        self.img_height_width_dict = {}
        self.p_url = ''
        self.URL = 'https://api.vk.com/method/photos.get'
        self.params = {
            'owner_id': input('Введите id пользователя ВК: '),
            'access_token': self.token,
            'album_id': 'profile',
            'extended': 1,
            'photo_sizes': 1,
            'count': input('Введите количество фотографий: '),
            'rev': 0,
            'v': '5.131'
        }

    def get_img_with_params(self):
        res = requests.get(self.URL, params=self.params)
        r = res.json()
        order_number = 0
        for v in r.values():
            for key, value in v.items():
                if key == 'items':
                    for _ in value:
                        img = r['response']['items'][order_number]['sizes'][-1]['url']
                        img_likes_count = r['response']['items'][order_number]['likes']['count']
                        img_size = r['response']['items'][order_number]['sizes'][-1]['type']
                        img_size_h = r['response']['items'][order_number]['sizes'][-1]['height']
                        img_size_w = r['response']['items'][order_number]['sizes'][-1]['width']
                        img_name = naming(img_likes_count, self.namelist)
                        img_hw = {'height': img_size_h, 'width': img_size_w, 'url': img}
                        self.img_height_width_dict[img_name] = img_hw
                        self.namelist.append(img_name)
                        with open(f' {img_name}.txt', 'w') as f:
                            json.dump(r, f)
                        data_dict = {'filename': f'{img_name}.jpg', 'size': f'{img_size}'}
                        self.data.append(data_dict)
                        self.data.clear()
                        data_dict.clear()
                        order_number += 1
