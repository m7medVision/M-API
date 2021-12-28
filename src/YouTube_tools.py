import requests
import re
from bs4 import BeautifulSoup
import json
def get_last_video_id_form_c(cid):
    """
    cid = channel id
    """
    headers = {
        'authority': 'www.youtube.com',
        'cache-control': 'max-age=0',
        'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="96", "Google Chrome";v="96"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'dnt': '1',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'service-worker-navigation-preload': 'true',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-user': '?1',
        'sec-fetch-dest': 'document',
        'accept-language': 'en-US,en;q=0.9',
        'cookie': 'GPS=1; YSC=ld3Ddx9mGaU; VISITOR_INFO1_LIVE=T0u5UGKumko; CONSISTENCY=AGDxDeNCVGYrAVEB2FSVf9eeRZcSvRwOtPLBOFjvp-KJEK5W1WjZW1gYb_uCL6NF1a-IIyaJ3_69-uLJZnaol2xGiIIDlKvwoAVUt3gCQo-DfH1oLq_PvfLmjewSh6pfxD4ZI1AiLDxpJtttcDpxMQ; PREF=tz=Asia.Dubai&f6=40000000',
    }
    cid        = str(cid)
    html       = requests.get('https://www.youtube.com/channel/{}/videos'.format(cid), headers=headers).text
    soup       = BeautifulSoup(html, 'lxml')
    script     = soup.find_all("script")[31]
    m          = re.search('var ytInitialData = (.+)[,;]{1}', str(script)).group(1)
    json_m     = json.loads(m)
    last_video = json_m['contents']['twoColumnBrowseResultsRenderer']['tabs'][1]['tabRenderer']['content']['sectionListRenderer']['contents'][0]['itemSectionRenderer']['contents'][0]['gridRenderer']['items'][0]['gridVideoRenderer']['videoId']
   
   
    return last_video