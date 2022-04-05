"""
Coded by @majhcc
"""
import requests
import lxml.html
from bs4 import BeautifulSoup


def get_google_results(query):
    res = requests.get(f'https://www.google.com/search?q=python', allow_redirects=True, headers={
                       'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36'})
    soup = BeautifulSoup(res.content, 'lxml')
    respon = soup.find_all('span', {'class': 'SJajHc NVbCr'})
    pageid = 0
    links = []
    for i in range(len(respon)+1):
        res = requests.get(f'https://www.google.com/search?q={query}&start={i*10}', allow_redirects=True, headers={
                           'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36'})
        html = lxml.html.fromstring(res.content)
        respon = html.xpath('//*[@class="yuRUbf"]/a/@href')
        links += respon
    return links
