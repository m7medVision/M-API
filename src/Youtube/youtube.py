import re
import requests
from bs4 import BeautifulSoup
import lxml.html

BASEURL = 'https://ytmp3to.com/api/single/'
def get_mp3(_id: str):
    url = BASEURL + "mp3/" + _id
    r = requests.get(url)
    html = lxml.html.fromstring(r.content)
    mp3_url = html.xpath('/html/body/a/@href')[0]
    return mp3_url

def get_videos(_id: str):
    url = BASEURL + "videos/" + _id
    r = requests.get(url)
    html = lxml.html.fromstring(r.content)
    video_url = html.xpath('/html/body/a/@href')[0]
    return video_url
