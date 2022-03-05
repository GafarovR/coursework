import requests


class YaUploader:

    def __init__(self):
        self.token = ''     # yandex token

    def get_headers(self):
        return {
            'Content-Type': 'application/json',
            'Authorization': 'OAuth {}'.format(self.token)
        }

    def add_folder(self):
        add_url = 'https://cloud-api.yandex.net/v1/disk/resources'
        headers = self.get_headers()
        params = {'path': 'Pictures'}
        res = requests.put(add_url, headers=headers, params=params)
        r = res.json()
        # if r['error'] == 'DiskPathPointsToExistentDirectoryError':
        #     return 'Папка с указанным именем уже существует'
        # else:
        return r

    def upload_by_url(self, pic_name, pic_url):
        upload_url = 'https://cloud-api.yandex.net/v1/disk/resources/upload'
        headers = self.get_headers()
        params = {
            'path': f'{pic_name}.jpg',
            'url': pic_url
        }
        res = requests.post(upload_url, headers=headers, params=params)
