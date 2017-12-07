# test_system.py
import requests
import json


def test_root(testing_server):
    expected_data = {
        "username": "ryan.rabello",
        "wwuid": "919428746",
        "roles": "forms-admin",
        "photo": None,
        "status": None,
        "full_name": "Ryan Rabello"
    }

    url = 'http://127.0.0.1:8888/'
    resp = requests.get(url)
    assert (resp.status_code == 200)
    assert (json.loads(resp.text) == expected_data)
