import requests
import lxml.html
def get_list():
    alist = []
    count = 0
    for i in range(1, 11):
            url = 'https://proxylist.geonode.com/api/proxy-list?limit=50000&page={}&sort_by=lastChecked'.format(i)
            response = requests.get(url)
            data = response.json()['data']
            for item in data:
                proxy = item['ip']
                port = item['port']
                aproxy = proxy + ':' + port
                alist.append(aproxy)
    alist = list( dict.fromkeys(alist) )
    return alist