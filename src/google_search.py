"""
Coded by @majhcc
"""
import requests
import lxml.html
from bs4 import BeautifulSoup


def get_google_results(query):
    res = requests.get(f'https://www.google.com/search?q={query}', allow_redirects=True, headers={
                       'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36'})
    soup = BeautifulSoup(res.content, 'lxml')
    respon = soup.find_all('span', {'class': 'SJajHc NVbCr'})
    links = []
    for i in range(len(respon)+1):
        res = requests.get(f'https://www.google.com/search?q={query}&start={i*10}', allow_redirects=True, headers={
                           'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36'})
        html = lxml.html.fromstring(res.content)
        respon = html.xpath('//*[@class="yuRUbf"]/a/@href')
        links += respon
    return links

def advanced_search(query, county, language) -> list:
    resp = requests.get(f'https://www.google.com/search?as_q={query}&lr=lang_{language}&cr=country{county}', allow_redirects=True, headers={
                          'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36'})
    soup = BeautifulSoup(resp.content, 'lxml')
    respon = soup.find_all('span', {'class': 'SJajHc NVbCr'})
    links = []
    for i in range(len(respon)+1):
        res = requests.get(f'https://www.google.com/search?as_q={query}&lr=lang_{language}&cr=country{county}&start={i*10}', allow_redirects=True, headers={
                           'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36'})
        html = lxml.html.fromstring(res.content)
        respon = html.xpath('//*[@class="yuRUbf"]/a/@href')
        links += respon
    return links


