import requests
import lxml.html
def get_list():
    list = []
    html = lxml.html.fromstring(requests.get('https://free-proxy-list.net/', headers={'User-Agent': 'Mozilla/5.0'}).text)
    for r in html.xpath('//*[@id="list"]/div/div[2]/div/table/tbody/tr[*]'):
        try:
            proxy = r.xpath('td[1]/text()')[0]
        except:
            proxy = None
        try:
            port = r.xpath('td[2]/text()')[0]
        except:
            port = None
        
        if proxy or port != None:
            aproxy = proxy + ':' + port
            list.append(aproxy)
    return list