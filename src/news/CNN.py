import requests
from bs4 import BeautifulSoup
def get_news():
    url = 'https://edition.cnn.com/world'
    res = requests.get(url)
    soup = BeautifulSoup(res.text, 'lxml')
    response = []
    for i in soup.find_all('h3', {'class':'cd__headline'}):
        headline = i.get_text().strip()
        response.append(
            {
            "url": 'https://edition.cnn.com{}'.format(i.find('a').get('href')),
            'headline': f'{headline}'
            }
        )
    return response