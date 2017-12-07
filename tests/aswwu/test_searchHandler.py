import requests
import json

def test_searchTest1(testing_server):
    expected_data = {'results': [{'username':'ryan.rabello',
                    'photo':'profiles/1718/00958-2019687.jpg',
                    'email':'ryan.rabello@wallawalla.edu',                                  
                    'full_name': 'Ryan Rabello',
                    'views':'9'}]}
    url = "http://127.0.0.1:8888/search/1718/ryan.rabello"
    resp = requests.get(url)
    assert (resp.status_code == 200)
    assert (json.loads(resp.text) == expected_data)
    
def test_searchTest2(testing_server):
    expected_data = {'results': [{'username':'john.doe',
                    'photo':'profiles/1718/00958-2019687.jpg',
                    'email':'',                                  
                    'full_name': 'John Doe',
                    'views':'6'}]}
    url = "http://127.0.0.1:8888/search/1718/john.doe"
    resp = requests.get(url)
    assert (resp.status_code == 200)
    assert (json.loads(resp.text) == expected_data)
 
def test_NotFound(testing_server):
    expected_data = {'results': []}
    url = "http://127.0.0.1:8888/search/1718/patty.dunp"
    resp = requests.get(url)
    assert (resp.status_code == 200)
    assert (json.loads(resp.text) == expected_data)

def test_offYear(testing_server):
    expected_data = {'results': []}
    url = "http://127.0.0.1:8888/search/1719/ryan.rabello"
    resp = requests.get(url)
    assert (resp.status_code == 200)
    assert (json.loads(resp.text) == expected_data)

#def test_views(testing_server): 
