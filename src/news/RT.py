"""
Coded by @majhcc
"""
import requests
from bs4 import BeautifulSoup
def get_news():
    res = requests.get('https://www.rt.com/news/')
    soup = BeautifulSoup(res.text, 'lxml')
    response = []
    for i in soup.find_all('a', {'class':'link link_hover'}):
            response.append(

                {
                "url": 'https://www.rt.com/{}'.format(i.get('href')),
                'headline': f'{i.get_text().strip()}'
                }
                
                        )
    return response