import requests


class YaUploader:

    def __init__(self, token):
        self.token = token

    def get_headers(self):
        return {
            'Content-Type': 'application/json',
            'Authorization': 'OAuth {}'.format(self.token)
        }

    def _get_upload_link(self, disk_file_path):
        upload_url = 'https://cloud-api.yandex.net/v1/disk/resources/upload'
        headers = self.get_headers()
        params = {'path': disk_file_path, 'overwrite': 'true'}
        res = requests.get(upload_url, headers=headers, params=params)
        return res.json()

    def upload(self, file_path, upload_filename):
        href = self._get_upload_link(disk_file_path=upload_filename).get('href', '')
        res = requests.put(href, data=open(file_path, 'rb'))
        res.raise_for_status()
        # if res.status_code == 201:
        #     print("Success")
