"""
Coded by @majhcc
"""
from bs4 import BeautifulSoup
import requests


def get_news():
    url = 'https://www.bbc.com/news'
    res = requests.get(url)
    soup = BeautifulSoup(res.text, 'lxml')
    response = []
    for i in soup.find_all('a', {'class': 'gs-c-promo-heading gs-o-faux-block-link__overlay-link gel-pica-bold nw-o-link-split__anchor'}):
        response.append(
            {
                "url": 'https://www.bbc.com{}'.format(i.get('href')),
                'headline': f'{i.get_text().strip()}'
            }
        )
    return response
# @app.get('/api/news/bbc')
# def news_bbc():
#     from src.news.BBC import get_news
#     try:
#         return {
#             'status': 'success',
#             'news': get_news()
#             }
#     except Exception as e:
#         data = {
#             'content': f'Get news from BBC api Error: ***{str(e)}***'
#         }
#         requests.post(WEBHOOKURL, data=data)
#         return {
#         'status': 'error'}
