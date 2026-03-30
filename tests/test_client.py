from unittest.mock import patch, Mock
from httpclient.client import HttpClient
from httpclient.cache import ResponseCache

def test_get_pass():
    with patch('httpclient.client.requests.get') as m:
        m.return_value = Mock(status_code=200)
        assert HttpClient().get('http://x').status_code == 200

def test_post_pass():
    with patch('httpclient.client.requests.post') as m:
        m.return_value = Mock(status_code=201)
        assert HttpClient().post('http://x', json={'a':1}).status_code == 201

def test_cache_hit_pass():
    c=ResponseCache()
    client=HttpClient(cache=c)
    with patch('httpclient.client.requests.get') as m:
        m.return_value=Mock(status_code=200)
        client.get('http://x')
        client.get('http://x')
        assert m.call_count==1

def test_put_pass():
    with patch('httpclient.client.requests.put') as m:
        m.return_value = Mock(status_code=200)
        assert HttpClient().put('http://x', json={'a': 1}).status_code == 200

def test_delete_pass():
    with patch('httpclient.client.requests.delete') as m:
        m.return_value = Mock(status_code=204)
        assert HttpClient().delete('http://x').status_code == 204
