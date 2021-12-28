import requests
import re
from bs4 import BeautifulSoup
import json
def get_last_video_id_form_c(cid):
    """
    cid = channel id
    """
    cid        = str(cid)
    html       = requests.get('https://www.youtube.com/channel/{}/videos'.format(cid), headers={'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36'}).text
    soup       = BeautifulSoup(html, 'lxml')
    script     = soup.find_all("script")[31]
    m          = re.search('var ytInitialData = (.+)[,;]{1}', str(script)).group(1)
    json_m     = json.loads(m)
    last_video = json_m['contents']['twoColumnBrowseResultsRenderer']['tabs'][1]['tabRenderer']['content']['sectionListRenderer']['contents'][0]['itemSectionRenderer']['contents'][0]['gridRenderer']['items'][0]['gridVideoRenderer']['videoId']
   
   
    return last_video