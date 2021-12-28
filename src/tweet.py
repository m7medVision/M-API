"""
Coded by @majhcc
"""
import requests
from requests.api import get
from src.random_useragent import random_useragent
def get_token():
    """
    Get download token
    """
    headers = {'User-Agent': random_useragent()}
    res = requests.get('https://twsaver.com/', headers=headers)
    from bs4 import BeautifulSoup
    soup = BeautifulSoup(res.text, 'html.parser')
    token = soup.find('input', {'name': 'token', 'id':'token'})['value']
    return token
def get_url_download(url):
    """
    Get url download
    """
    
    headers = {'User-Agent': random_useragent(),
               'Referer': 'https://twsaver.com/',
               'X-Requested-With': 'XMLHttpRequest',
               'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
               'Accept': '*/*'}

    res = requests.post('https://twsaver.com/system/action.php', data={'url': url, 'token': get_token()}, headers=headers)
    r = res.json()
    r.pop('client_ip')
    r['dev'] = '@majhcc'
    return r

# print(get_url_download('https://twitter.com/saudistuff/status/1459470906250641408'))
# for i in get_url_download('https://twitter.com/saudistuff/status/1459470906250641408', get_token())['links']:
#     print(i['url'])