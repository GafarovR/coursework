from vk import Vk
from yandex import YaUploader
from tqdm import tqdm
from pprint import pprint


def get_largest_images(d, count=5):  # сортировка по высоте/ширине (в sorted поменять x[1] и x[2] местами)
    img_list = []
    for kk, vv in d.items():
        for parameter, measure in vv.items():
            if parameter == 'height':
                l1 = [kk, vv['height'], vv['width']]
                img_list.append(l1)
    img_list = sorted(img_list, key=lambda x: (-x[1], -x[2]))
    del img_list[count:-1]
    return img_list


def get_largest_images2(d, count=5):  # сортировка по произведению высоты на ширину
    img_list = []
    for kk, vv in d.items():
        for parameter, measure in vv.items():
            if parameter == 'height':
                l1 = [kk, vv['height']*vv['width'], vv['url']]
                img_list.append(l1)
    img_list = sorted(img_list, key=lambda x: -x[1])
    del img_list[count:]
    return img_list


if __name__ == '__main__':
    vk = Vk()
    vk.params['owner_id'] = vk.get_profile_id()
    vk.get_img_with_params()
    l_dict = vk.img_height_width_dict.copy()
    largest_image_ids = get_largest_images2(l_dict)
    uploader = YaUploader()
    uploader.add_folder()
    for element in tqdm(largest_image_ids, bar_format='{l_bar}{bar:20}|{n_fmt}/{total_fmt}'):
        img_name = f'Pictures/{element[0]}'
        file_path = element[2]
        uploader.upload_by_url(img_name, file_path)
