import requests
import lxml.html
def get_list():
    alist = []
    count = 0
    for i in range(1, 5):
            url = 'https://proxylist.geonode.com/api/proxy-list?limit=50&page={}&sort_by=lastChecked'.format(i)
            response = requests.get(url, timeout=100, headers={'User-Agent': 'Mozilla/5.0'})
            data = response.json()['data']
            for item in data:
                proxy = item['ip']
                port = item['port']
                aproxy = proxy + ':' + port
                alist.append(aproxy)
    alist = list( dict.fromkeys(alist) )
    return alist