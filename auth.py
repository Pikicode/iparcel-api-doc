# python 3.8.1

import uuid
# request requests==2.25.1
import requests

class Config:
    def __init__(self, host=None, token:str=None):
        self.host = host
        self.headers = {
            # test only.
            'Authorization': 'Token {}'.format(token)
        }

    def post(self, url, payload={}):
        return requests.post(
            url=self.host + url, headers=self.headers, data=payload)

    def get(self, url, payload={}):
        return requests.get(
            url=self.host + url, headers=self.headers, data=payload) 

    def put(self, url, payload={}):
        return requests.put(
            url=self.host + url, headers=self.headers, data=payload) 

    def path(self, url, payload={}):
        return requests.patch(
            url=self.host + url, headers=self.headers, data=payload)

    def get_warehouses(self):
        res = self.get('/api/inventory/warehouses/')
        print('Warehouses: ', res.json())
        return res.json()
    


BASE_URL = 'http://dev.goparcelpro.com/'
TOKEN = 'bdf6677b8c52fa8489d29263fb401f85a3d84f26'
config = Config(BASE_URL, TOKEN)
