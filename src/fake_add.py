# function that bring fake address from https://www.fakeaddressgenerator.com/
"""
Coded by @majhcc
"""
import requests


def fake_add():
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36 Edg/96.0.1054.29',
        'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'accept': 'application/json, text/javascript, */*; q=0.01',
        'x-requested-with': 'XMLHttpRequest',
        'origin': 'https://www.prepostseo.com',
    }

    data = {
        'lang': 'en_US'
    }

    response = requests.post(
        'https://www.prepostseo.com/frontend/fakeAddressGenerator', headers=headers, data=data)
    json = response.json()[0]
    name = json['name']
    json['FristName'] = name.split(' ')[-2]
    json['LastName'] = name.split(' ')[-1]
    return json
