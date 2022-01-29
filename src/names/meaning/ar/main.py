import requests
import re
from bs4 import BeautifulSoup
import urllib.parse

def get_meaing(name):
    if re.match(r'[\u0600-\u06FF\s]+', name):
        headers = {
            'authority': 'meaningnames.net',
            'pragma': 'no-cache',
            'cache-control': 'no-cache',
            'sec-ch-ua': '" Not;A Brand";v="99", "Google Chrome";v="97", "Chromium";v="97"',
            'dnt': '1',
            'sec-ch-ua-mobile': '?0',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36',
            'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
            'accept': '*/*',
            'x-requested-with': 'XMLHttpRequest',
            'sec-ch-ua-platform': '"Windows"',
            'origin': 'https://meaningnames.net',
            'sec-fetch-site': 'same-origin',
            'sec-fetch-mode': 'cors',
            'sec-fetch-dest': 'empty',
            'referer': 'https://meaningnames.net/Arabic-nationality-1',
            'accept-language': 'en-US,en;q=0.9,ar;q=0.8',
            'cookie': 'PHPSESSID=hub035bbo4otqkiu59nqh1e7k3; __cf_bm=0Z33mepfVswuGPlEPjvvp6Zsz_FeH2A.WNllknpgJSI-1643461761-0-Aeq4xzYkbmLH6e5DS6rO0iK9WW7e515h+RNOPVAFUXIBDnfQwHWGNkd2SquVHgFUUc2WlyzEs+XH48QEGLQ8cnA=; _ga=GA1.2.83370815.1643461815; _gid=GA1.2.296991169.1643461822',
        }

        data = {
        'name': name,
        'ajax': 'TRUE'
        }

        response = requests.post('https://meaningnames.net/mean.php', headers=headers, data=data)
        soup = BeautifulSoup(response.text, 'lxml')
        try:
            meaning = soup.find('h3', {'style': "line-height: 215%;"}).text
            img = soup.find('img').get('src')
            return {
                'meaning': meaning,
                'img': img,
                'status': True
                }
        except:
            return {'meaning': '', 'img': '', 'status': False}
    else:
        return {'meaning': '', 'img': '', 'status': False}