"""
Coded by @majhcc
"""
import requests
import json
from bs4 import BeautifulSoup
def short_url(url,SUFFIX):
    res = requests.get('https://v.ht/')
    PHPSESSID = res.cookies['PHPSESSID']
    data = {
        'txt_url': url,
        'txt_name': SUFFIX,
    }
    headers = {
        'Accept': '*/*',
        'Accept-Encoding': 'gzip, deflate, br',
        'Connection': 'keep-alive',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Cookie': "PHPSESSID={}".format(PHPSESSID),
        'Host': 'v.ht',
        'Origin': 'https://v.ht',
        'Referer': 'https://v.ht/',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36 Edg/96.0.1054.29',
        'X-Requested-With': 'XMLHttpRequest'
    }
    res = requests.post('https://v.ht/processreq.php', headers=headers, data=data, cookies={'PHPSESSID': PHPSESSID})
    soup = BeautifulSoup(res.text, 'html.parser')
    try:
        url = soup.find('input', {'name': 'link1'})['value']
        return {
            'url': url,
            'dev': "@majhcc"
        }
    except:
        return {
            'error': 'Error: Can not get link',
            'dev': "@majhcc"
        }