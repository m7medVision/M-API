from bs4 import BeautifulSoup
import re
import ast
import requests
from telegram import user
def get_last_video_id(username):
    """
    Get the last video id from a user's profile page.
    """
    headers = {
        'authority': 'www.tiktok.com',
        'pragma': 'no-cache',
        'cache-control': 'no-cache',
        'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="96", "Google Chrome";v="96"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'dnt': '1',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-user': '?1',
        'sec-fetch-dest': 'document',
        'referer': 'https://www.tiktok.com/',
        'accept-language': 'en-US,en;q=0.9,ar;q=0.8',
        }

    response = requests.get('https://www.tiktok.com/@{}'.format(username), headers=headers)

    soup = BeautifulSoup(response.text, 'lxml')

    lastvideoid = ast.literal_eval("["+re.search(r'"ItemList":{"user-post":{"list":\[(.*?)\]', soup.find_all('script')[5].text.strip().replace('window[\'SIGI_STATE\']=', '')).group(1)+"]")[0]
    return lastvideoid