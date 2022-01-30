import requests
import json

class Client:
    def __init__(self, base_url):
        self.base_url = base_url

    def upload(self, file_path):
        url = self.base_url + "/api/file"

        files={'file': open(file_path,'rb')}

        return requests.request("POST", url, files=files)

    def get_all(self):
        url = self.base_url + "/api/file-info"
        return requests.request("GET", url, headers={}, data={})

    def download(self, name):
        url = self.base_url + "/api/file/" + name
        data = requests.request("GET", url, headers={}, data={})
        with open(name, 'wb') as f:
            f.write(data.content)

    def delete(self, name):
        url = self.base_url + "/api/file/" + name
        return requests.request("DELETE", url, headers={}, data={})