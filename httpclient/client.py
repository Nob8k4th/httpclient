import requests

class HttpClient:
    def __init__(self, cache=None):
        self.cache=cache
    def get(self,url,headers=None):
        key=(url, tuple(sorted((headers or {}).items())))
        if self.cache:
            c=self.cache.get(key)
            if c is not None:
                return c
        resp=requests.get(url, headers=headers)
        if self.cache:
            self.cache.set(key, resp)
        return resp
    def post(self,url,json=None):
        return requests.post(url, json=json)
    def put(self,url,json=None):
        return requests.put(url, json=json)
    def delete(self,url):
        return requests.delete(url)
