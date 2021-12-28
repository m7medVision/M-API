from bs4 import BeautifulSoup
import requests

def get_news():
    url = 'https://www.nytimes.com/international/section/world'
    res = requests.get(url)
    soup = BeautifulSoup(res.text, 'lxml')
    response = []
    for i in soup.find_all('h2', {'class':'css-byk1jx e1hr934v1'}):
        headline = i.get_text().strip()
        response.append(
            {
            "url": 'https://www.nytimes.com/{}'.format(i.find('a').get('href')),
            'headline': f'{headline}'
            }
        )
    return response
if __name__ == '__main__':
    print(get_news())
    print(len(get_news()))