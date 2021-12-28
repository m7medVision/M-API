from bs4 import BeautifulSoup
import requests

def get_news():
    url = 'https://www.foxnews.com/'
    res = requests.get(url)
    soup = BeautifulSoup(res.text, 'lxml')
    response = []
    for i in soup.find_all('h2', {'class':'title'}):
        headline = i.get_text().strip()
        response.append(
            {
            "url": i.find('a').get('href').replace('//', ''),
            'headline': f'{headline}'
            }
        )
    return response